"""
This module holds all the global xpf variables and gives access to them
via getter and setter functions.

The utilisation of getters/setters is to ensure no single module caches
the result of a variable after its changed. Variables should only be
accessed via the functions and never directly.
"""
# -- This is what we use to track whether our server is accessible.
# -- A value of -1 means the status test has not been performed. True means
# -- the server is accessible and False means the server is not accesible.
_SERVER_STATUS = -1

# -- This is the maximum amount of time a single perforce call is allowed
# -- to take before a default value is returned.
_TIMEOUT = 2

# -- Stores the currently active user as defined by p4 set
_USER = ''

# -- Stores the currently active port/server as defined by p4 set
_PORT = None

# -- Stores the currently active client as defined by p4 set
_CLIENT = None

# -- If true all the calls to p4 will be logged to the output
_DEBUG = False

# -- Stores the currently active host as defined in p4 set
_HOST = None


# ------------------------------------------------------------------------------
def get_server_status():
    return _SERVER_STATUS


# ------------------------------------------------------------------------------
def set_server_status(value):
    global _SERVER_STATUS
    _SERVER_STATUS = value


# ------------------------------------------------------------------------------
def get_timeout():
    return _TIMEOUT


# ------------------------------------------------------------------------------
def set_timeout(value):
    global _TIMEOUT
    _TIMEOUT = value


# ------------------------------------------------------------------------------
def get_user():
    return _USER


# ------------------------------------------------------------------------------
def set_user(value):
    global _USER
    _USER = value


# ------------------------------------------------------------------------------
def get_port():
    return _PORT


# ------------------------------------------------------------------------------
def set_port(value):
    global _PORT
    _PORT = value


# ------------------------------------------------------------------------------
def get_client():
    return _CLIENT


# ------------------------------------------------------------------------------
def set_client(value):
    global _CLIENT
    _CLIENT = value


# ------------------------------------------------------------------------------
def get_debug():
    return _DEBUG


# ------------------------------------------------------------------------------
def set_debug(value):
    global _DEBUG
    _DEBUG = value


# ------------------------------------------------------------------------------
def get_host():
    return _HOST


# ------------------------------------------------------------------------------
def set_host(value):
    global _HOST
    _HOST = value
