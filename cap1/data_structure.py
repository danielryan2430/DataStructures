"""
Data structure base class:

This class guarantees that all of my DSes have the same functions, so that I can get a correct
"function not implemented" error, rather than a typing based error that would be harder to debug.
"""


class DataStructureBase(object):

    @property
    def name(self):
        raise NotImplementedError()

    def insert(self, value):
        raise NotImplementedError()

    def lookup(self, value):
        raise NotImplementedError()

    def delete(self, value):
        raise NotImplementedError()
