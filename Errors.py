

class Error(Exception):
    """Base class for other exceptions"""
    pass


class NotInRangeError(Error):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(Error):
    """Raised when the input value is too large"""
    pass

class Occupied(Error):
    """Raised when the space on the board is occupied"""
    pass












