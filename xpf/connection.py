"""
This module handles the connection and serve accessibility methods. All calls
should be routed through here to ensure for a consistent result
"""
import sys
import time
import marshal
import threading
import subprocess

from . import variables


# ------------------------------------------------------------------------------
def safe_run(*args, **kwargs):
    """
    Every call made through xpf is processed through this function. This manages
    the global xpf variables and kwargs (such as timeout, return_type, form,
    marshal, port and client).

    This will also manage the timeout logic, returning the default_value if
    ever the timeout is exceeded.

    It also manages the format of arguments coming in, wrapping all strings
    in quotes to ensure thorough compatibility as well as constructing the
    commandline.

    :return: bool 
    """

    # -- Pull our all our special arguments
    timeout = kwargs.get(
        'timeout',
        variables.get_timeout(),
    )

    return_type = kwargs.get(
        'return_type',
        None,
    )

    # -- Forms are used to inject data to p4
    form = kwargs.get(
        'form',
        None,
    )

    marshal_result = kwargs.get(
        'marshal',
        True,
    )

    port = kwargs.get(
        'port',
        variables.get_port(),
    )

    client = kwargs.get(
        'client',
        None
    )

    # -- Define our mandatory elements for the perforce command
    cmd = [
        'p4',
        '-G' if marshal_result else '',
    ]

    # -- Add the port and client if they are given. These have to be
    # -- added before the command
    if port:
        cmd.extend(['-p', port])

    if client:
        cmd.extend(['-c', client])

    # -- Now extend it with all the arguments coming into the
    # -- the function
    cmd.extend(args)

    # -- Finally, construct our execution string
    formatted_items = list()
    for item in cmd:
        item = _stringify(item)
        if item:
            formatted_items.append(item)

    # -- Join it all together
    exec_str = ' '.join(formatted_items)

    # -- If we're meant to log debug info print off the command
    # -- we're about to run
    if variables.get_debug():
        print('xpf :: %s' % exec_str)

    # -- Open a process to run an external call
    thread = ThreadedP4Call(
        exec_str,
        form=form,
        marshal_result=marshal_result,
    )

    # -- Start the execution thread and being the timer. Python 3 has a
    # -- lot of the timeout functionality already built into subprocess
    # -- but we need to by python 2 compatible.
    thread.start()
    start_time = time.time()

    # -- Loop for the duration of the call, monitoring how long
    # -- its taking
    while not thread.complete:

        # -- Determine how long we have been running the call
        current_time = time.time()
        delta_time = (current_time - start_time)  # Convert to seconds

        # -- If we exceeded our timeout period we need to terminate
        # -- our call and return our default return type rather than
        # -- the actual return value
        if delta_time > timeout:
            print('xpf :: timing out (after %ss)...' % timeout)
            thread.process = None
            del thread

            return return_type

    return thread.results


# ------------------------------------------------------------------------------
def is_accessible(force=False):
    """
    This is a 'run once' test to check whether the perforce server
    is accessible. The test can forcibly be rerun by providing the
    force argument.

    :param force: If True then the test will be run even if it has already
        been run before.
    :type force: bool

    :return: True if the server is accessible
    """
    server_status = variables.get_server_status()

    # -- If we have never been run before, perform a full connection
    # -- test and scrape
    if server_status == -1 or force:
        initialise_variables()

    return variables.get_server_status()


# ------------------------------------------------------------------------------
def initialise_variables():
    """
    This will perform a test against the perforce server and scrape the
    environment for various bits of data which we do not expect to change
    unless specified. This makes the module far more performant.

    :return:
    """
    # -- To get here we need to initalise all our settings.
    server_result = safe_run(
        'info',
        timeout=1,
        return_type=None
    )

    # -- If the server was not accessible then there is little more to do
    if not server_result:
        variables.set_server_status(False)
        return False

    variables.set_host(server_result[0]['clientHost'])

    # -- We can access the server, so update that setting, then continue
    # -- to initialise the rest of the module variables
    variables.set_server_status(True)

    # Set the user settings
    p4_set_data = safe_run(
        'set',
        marshal=False,
    )

    if not p4_set_data:
        variables.set_server_status(False)
        return False

    p4_set_data = p4_set_data.replace('(set)', '').split()

    for item in p4_set_data:
        if '=' not in item:
            continue

        k, v = item.split('=')

        if k == 'P4CLIENT':
            variables.set_client(v)

        elif k == 'P4USER':
            variables.set_user(v)

        elif k == 'P4PORT':
            variables.set_port(v)


# ------------------------------------------------------------------------------
def _stringify(item):
    """
    Private funtion which wraps all items in quotes to protect from paths
    being broken up. It will also unpack lists into strings

    :param item: Item to stringify.

    :return: string
    """
    if isinstance(item, (list, tuple)):
        return '"' + '" "'.join(item) + '"'

    if isinstance(item, str) and len(item) == 0:
        return None

    return '"%s"' % item


# ------------------------------------------------------------------------------
class ThreadedP4Call(threading.Thread):
    """
    All our calls are threaded to allow for timeouts to occur in both
    Python2 and Python3
    """

    # --------------------------------------------------------------------------
    def __init__(self, cmd, form=None, marshal_result=True):
        super(ThreadedP4Call, self).__init__()

        self.cmd = cmd
        self.form = form
        self.marshal = marshal_result

        self.process = None
        self.complete = False
        self.results = list()

    # --------------------------------------------------------------------------
    def run(self):

        # -- This is pretty much a copy/paste of the p4 example of using
        # -- -G. We kick off a process, get the process input and output,
        # -- injecting any form informaiton before reading the output
        p = subprocess.Popen(
            self.cmd,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            shell=True,
        )

        (pi, po) = (p.stdin, p.stdout)

        if self.form:
            marshal.dump(self.form, pi, 0)
            pi.close()

        # -- How we read the output depends a lot on whether we need
        # -- to marshal or not. If we do, we must conform specific
        # -- dictionary standards which can differ between python2 and
        # -- python3 (py2 gives strings, py3 gives bytes)
        if self.marshal:
            records = []
            try:
                while True:
                    records.append(
                        self._byte_dict_to_str_dict(
                            marshal.loads(po.read())
                        )
                    )

            except EOFError:
                pass

            self.results = records

        else:
            self.results = po.read().decode('utf-8')

        # -- By setting this to True we know we're completely finished.
        self.complete = True

    # --------------------------------------------------------------------------
    @staticmethod
    def _byte_dict_to_str_dict(dictionary):
        """
        This ensures that the dictionary has any keys and values converted
        from bytes to strings.
        
        :param dictionary: 
        :return: 
        """
        if sys.version_info.major < 3:
            return dictionary

        converted_output = dict()

        # -- Cycle our items and convert any bytes to strings
        for k, v in dictionary.items():
            k = k.decode('utf8') if isinstance(k, bytes) else k
            v = v.decode('utf8') if isinstance(v, bytes) else v

            # -- Update our dictionary data
            converted_output[k] = v

        return converted_output
