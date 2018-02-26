"""
Consulate Exceptions

"""


class ConsulateException(Exception):
    """Base Consul exception"""


class ServerError(ConsulateException):
    """An internal Consul server error occurred"""


class ACLDisabled(ConsulateException):
    """Raised when ACL related calls are made while ACLs are disabled"""


class Forbidden(ConsulateException):
    """Raised when ACLs are enabled and the token does not validate"""


class NotFound(ConsulateException):
    """Raised when an operation is attempted with a value that can not be
    found.

    """


class LockFailure(ConsulateException):
    """Raised by :class:`~consulate.api.lock.Lock` if the lock can not be
    acquired.

    """
