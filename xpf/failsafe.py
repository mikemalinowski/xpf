"""
This holds a series of decorators designed to faux the return values
of functions in the absence of a perforce server, or a server which
is not responsive within a reasonable amount of time
"""
from . import connection


# --------------------------------------------------------------------------
def return_true(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return True
        return func(*args, **kwargs)

    return wrapper


# --------------------------------------------------------------------------
def return_false(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return False
        return func(*args, **kwargs)

    return wrapper


# --------------------------------------------------------------------------
def return_none(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return None
        return func(*args, **kwargs)

    return wrapper


# --------------------------------------------------------------------------
def return_list(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return list()
        return func(*args, **kwargs)

    return wrapper


# ------------------------------------------------------------------------------
def return_dict(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return dict()
        return func(*args, **kwargs)

    return wrapper


# ------------------------------------------------------------------------------
def return_string(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return ''
        return func(*args, **kwargs)

    return wrapper
