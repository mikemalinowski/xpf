"""
This holds higher level functionality for common place behaviours. 
"""
from . import direct
from . import failsafe
from . import variables


# ------------------------------------------------------------------------------
@failsafe.return_false
def sync(files=None, cl_num=None, force=False, revision=None, *args, **kwargs):
    """
    This will sync all the files passed or alternatively a change list
    number.

    If a change list number is given then the files for the change 
    will be inspected and synced.

    :param files: Optional list of files to sync to, or a single filepath
    :type files: list(str, str, ...) or str

    :param cl_num: Optional changelist number, if given all the files within
        that changelist will be used.
    :type cl_num: int

    :param force: If true a force sync will occur
    :type force: bool

    :param revision: If a revision number is given, the file(s) will be
        synced to that version
    :type revision: int

    :param kwargs: Any additional arguments you want to pass to the perforce
        call

    :return: 
    """
    if not files:
        files = list()

    if not isinstance(files, (list, tuple)):
        files = [files]

    # -- If we're given a changelist number we need to add all the files
    # -- from that change list number to our file list
    if cl_num:
        query = direct.describe(cl_num)
        files.extend(query[0]['depotFile'])

    # -- If we're given a specific revision we should tag
    # -- that onto the end of the file paths
    if revision:
        for idx, filepath in enumerate(files):
            files[idx] = '%s#%s' % (filepath, revision)

    if force:
        results = direct.sync(
            '-f',
            files,
            *args,
            **kwargs
        )
    else:
        results = direct.sync(
            files,
            *args,
            **kwargs
        )

    for result in results:
        if result.get('code') == 'error' and 'up-to-date' not in result['data']:
            return False

    return True


# ------------------------------------------------------------------------------
@failsafe.return_false
def add_to_changelist(files, description='default', change_id=None):
    """
    This will add the list of files being given to a changelist with the
    given description for the current user. This will handle the semantics
    around edit and add, as well as moving any of the given files which may
    already be in pre-existing changelists.

    You can define the changelist either through a description or through
    a specific changelist number.

    If a description is given, and no changelist can be found with that
    description then a new changelist will be created.

    :param files: Optional list of files to sync to, or a single filepath
    :type files: list(str, str, ...) or str

    :param description: The description to assign to the changelist if it
        does not exist.
    :type description: str

    :param change_id: If given, this is the changelist which all the files
        will be added to.

    :return: the changelist id number which was added/used
    """
    if not isinstance(files, (list, tuple)):
        files = files

    # -- If we're given a changelist description we need to make a change
    # -- list with that description if it does not already exist
    if not change_id:
        change_id = get_changelist(description)

    # -- The more we batch up the commands the faster
    # -- this will be, so we create a list of all the files
    # -- we can add, and edit seperately so we can run it
    # -- together
    operations = dict(
        add=[],
        edit=[],
    )

    # -- Check if the file already exists in perforce, if it does
    # -- we edit, otherwise we add
    for file_path in files:
        try:
            if len(direct.fstat(file_path)):
                operations['edit'].append(file_path)
            else:
                operations['add'].append(file_path)

        except:
            operations['add'].append(file_path)

    # -- We can now do the actions in two steps
    for op in ['add', 'edit']:
        if len(operations[op]) == 0:
            continue

        # -- Run the required operation (add or edit)
        direct.run(
            op,
            '-c',
            change_id,
            operations[op],
        )

    # -- Ensure all the files are in the same change list regardless
    # -- of whether or not they were already opened
    direct.reopen(
        '-c',
        change_id,
        files,
    )

    return change_id


# ------------------------------------------------------------------------------
@failsafe.return_true
def have(files, *args, **kwargs):
    """
    Performs a have operation and checks the details returned. This will then
    return True if the file exists. If multiple files exist then all the files
    need to exist to get a True return

    :param files: Optional list of files to sync to, or a single filepath
    :type files: list(str, str, ...) or str

    :param kwargs: Any additional arguments you want to pass to the perforce
        call

    :return: 
    """

    if not isinstance(files, (list, tuple)):
        files = files

    f_list = '" "'.join(files)
    f_list = '"%s"' % f_list
    results = direct.have(f_list, *args, **kwargs)

    if not results:
        return False

    for result in results:
        if 'not on client' in str(result):
            return False

    return True


# ------------------------------------------------------------------------------
@failsafe.return_none
def get_changelist(description, **kwargs):
    """
    This will attempt to find the changelist number by looking at the current
    users changelists for a changelist with a matching description (case
    sensitive).

    If no changelist is found then a new changelist will be created with that
    given description and the id of the changelist returned.

    :param description: The description to assign to the changelist if it
        does not exist.
    :type description: str

    :param kwargs: Any additional arguments you want to pass to the perforce
        call

    :return: the changelist id number which was added/used
    """
    # -- Execute our command
    current_changes = direct.changes(
        '-s',
        'pending',
        '-l',
        '-u',
        variables.get_user(),
        **kwargs
    )

    # -- This can occur if the server is offline
    if not current_changes:
        return None

    # -- Cycle the results, and check whether the description matches
    # -- any of the found changelists
    change_id = 0
    for change in current_changes:
        if description.lower().strip() == change['desc'].lower().strip():
            return int(change['change'])

    # -- If we do not have a pre-existing one, lets make one
    if not change_id:
        result = direct.changelist(
            '-i',
            form={
                'Change': 'new',
                'Status': 'new',
                'Description': str(description),
            },
            **kwargs
        )
        return int(result[0]['data'].split()[1])

    # -- Fallback, something has gone horribly wrong!
    return None


# ------------------------------------------------------------------------------
@failsafe.return_list
def workspace_names():
    """
    This returns a list of workspace (client) names which are usable for the
    current user and host.

    :return: list(str, str, ...) 
    """
    client_data = direct.run(
        '-H',
        variables.get_host(),
        'clients',
        '-u',
        variables.get_user(),
    )

    return [
        workspace['client']
        for workspace in client_data
        if workspace['Host'] == variables.get_host()
    ]


# ------------------------------------------------------------------------------
@failsafe.return_string
def current_workspace():
    """
    Returns the currently active (Default) workspace
    
    :return: str
    """
    return variables.get_client()


# ------------------------------------------------------------------------------
@failsafe.return_none
def changelist(filepath):
    """
    Returns the changelist number which the filepath is currently marked for
    edit within.

    :param filepath: Filepath to find
    :type filepath: str

    :return: int 
    """
    change_number = direct.opened(filepath)[0]
    return change_number['change']


# ------------------------------------------------------------------------------
@failsafe.return_false
def submit_files(files, description=None):
    """
    This will submit the given files under a changelist with the given
    description. If all the files are all already under the same changelist
    with the right description a straight submit is performed.

    If no changelist exists with the given description then a new changelist
    will be created.

    If the given files are currently spread across multiple changelists (or
    are in a different changelist to the one expected) they will be moved to
    the submission changelist prior to performing the submit.

    :param files: Optional list of files to sync to, or a single filepath
    :type files: list(str, str, ...) or str

    :param description: The description to assign to the changelist if it
        does not exist.
    :type description: str

    :return: submission changelist number
    """
    if not isinstance(files, (list, tuple)):
        files = [files]

    # -- If all the files are in the same changelist, submit it
    cl_number = changelist(files[0])

    # -- Get a full list of files in the change list
    cl_description = direct.describe(cl_number)[-1]

    local_files = [
        direct.where(depot_file)[0]['path']
        for depot_file in cl_description['depotFile']
    ]

    all_files_in_cl = True

    for local_file in local_files:
        if local_file not in files:
            all_files_in_cl = False
            break

    if not all_files_in_cl:
        add_to_changelist(
            files,
            description=description,
        )

    return direct.submit(
        '-c',
        cl_number,
    )
