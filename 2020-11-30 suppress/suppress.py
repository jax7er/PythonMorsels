from contextlib import contextmanager
from sys import exc_info


class SuppressedError:
    def __init__(self):
        self.exception = None
        self.traceback = None


@contextmanager
def suppress(*errors):
    se = SuppressedError()

    try:
        yield se
    except errors:
        _, se.exception, se.traceback = exc_info()
        return True
    finally:
        pass
