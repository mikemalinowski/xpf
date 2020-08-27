"""
This module contains classes which are contextual and useful
when wanting to change states for a specific period.
"""
from . import assist
from . import variables


# ------------------------------------------------------------------------------
class ConnectionDetails(object):
    """
    Allows the defining of default connection settings within the
    scope of the classes context
    """

    # --------------------------------------------------------------------------
    def __init__(self, port=None, client=None, host=None):

        # -- Store the incoming variables
        self.port = port
        self.client = client
        self.host = host

        self._original_port = None
        self._original_client = None
        self._original_host = None

    # --------------------------------------------------------------------------
    def __enter__(self):

        # -- Store the current state
        self._original_client = variables.get_client()
        self._original_host = variables.get_host()
        self._original_port = variables.get_port()

        # -- Set our details
        variables.set_port(self.port or self._original_port)
        variables.set_host(self.host or self._original_host)
        variables.set_client(self.client or self._original_client)

    # --------------------------------------------------------------------------
    def __exit__(self, exc_type, exc_val, exc_tb):

        # -- Restore our variables
        variables.set_port(self._original_port)
        variables.set_host(self._original_host)
        variables.set_client(self._original_client)


# ------------------------------------------------------------------------------
class EditAndSubmit(object):
    """
    This will take in a series of files, edit (or add) the files to
    a changelist, and on exit they shall be submitted.

    :param files: Optional list of files to sync to, or a single filepath
    :type files: list(str, str, ...) or str

    :param description: The description to assign to the changelist if it
        does not exist.
    :type description: str

    :param change_id: If given, this is the changelist which all the files
        will be added to.
    :type change_id: int

    :param raise_on_failure: If True, then any file that could not be checked
        out will raise an exception. If False they will be ignored.
    :type raise_on_failure: bool

    :param kwargs: Any additional arguments will be passed to all perforce
        calls
    :type kwargs: variable
    """

    # --------------------------------------------------------------------------
    def __init__(self,
                 files,
                 description='default',
                 change_id=None,
                 raise_on_failure=False,
                 **kwargs):

        # -- Store the incoming variables
        self.files = files
        self.description = description
        self.change_id = change_id
        self.raise_on_failure = raise_on_failure
        self.kwargs = kwargs

    # --------------------------------------------------------------------------
    def __enter__(self):

        # -- On enter we need to add the files to the change list
        self.change_id = assist.add_to_changelist(
            self.files,
            self.description,
            self.change_id,
            **self.kwargs
        )

        # -- If we need to raise an exception on failure we need
        # -- to check if any failures occurred.
        if self.raise_on_failure:
            if not assist.is_editable(self.files):
                raise Exception('Not all files are editable')

    # --------------------------------------------------------------------------
    def __exit__(self, exc_type, exc_val, exc_tb):

        # -- On exit, we need to submit the changelist
        assist.submit_files(
            self.files,
            change_id=self.change_id,
        )
