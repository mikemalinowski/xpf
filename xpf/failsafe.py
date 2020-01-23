"""
This holds a series of decorators designed to faux the return values
of functions in the absence of a perforce server, or a server which
is not responsive within a reasonable amount of time
"""
import sys
from . import connection


# --------------------------------------------------------------------------
def return_true(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return True

        try:
            return func(*args, **kwargs)

        except BaseException:
            print(str(sys.exc_info()))
            return True

    return wrapper


# --------------------------------------------------------------------------
def return_false(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return False

        try:
            return func(*args, **kwargs)

        except BaseException:
            print(str(sys.exc_info()))
            return False

    return wrapper


# --------------------------------------------------------------------------
def return_none(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return None

        try:
            return func(*args, **kwargs)

        except BaseException:
            print(str(sys.exc_info()))
            return None

    return wrapper


# --------------------------------------------------------------------------
def return_list(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return list()

        try:
            return func(*args, **kwargs)

        except BaseException:
            print(str(sys.exc_info()))
            return []

    return wrapper


# ------------------------------------------------------------------------------
def return_dict(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return dict()

        try:
            return func(*args, **kwargs)

        except BaseException:
            print(str(sys.exc_info()))
            return dict()

    return wrapper


# ------------------------------------------------------------------------------
def return_string(func):
    def wrapper(*args, **kwargs):
        if not connection.is_accessible():
            return ''

        try:
            return func(*args, **kwargs)

        except BaseException:
            print(str(sys.exc_info()))
            return ''

    return wrapper
