from linked_list import LinkedListStepCounter
from data_structure import DataStructureBase

"""
This hashtable h

"""


class HashTableChainingStepCounter(DataStructureBase):
    def __init__(self, capacity=1001):
        self._capacity = capacity
        self._size = 0
        self._data = [LinkedListStepCounter() for _ in range(capacity)]

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        self._data = value

    def _hash(self, key):
        """

        :param key: string
        :return: int (hashed value)
        In order to make chaining significantly more likely, this table's hashing function is purposely high on collisions
        """
        return sum(bytearray(key)) % self._capacity

    def insert(self, value):
        """

        :param value: string
        :return: int (num steps to insert)
        """
        hash_key = self._hash(value)
        return 1 + self.data[hash_key].insert(value)

    def lookup(self, key):
        """

        :param key: string
        :return: int (num steps to lookup)
        """
        hash_key = self._hash(key)
        chain_steps = self.data[hash_key].lookup(key)
        if chain_steps != -1:
            return chain_steps + 1
        else:
            return -1

    @property
    def name(self):
        return 'hash_table_with_chaining'

    def delete(self, key):
        """

        :param key: string
        :return: int (num steps to delete
        """
        hash_key = self._hash(key)
        chain_steps = self.data[hash_key].delete(key)
        if chain_steps != -1:
            return chain_steps + 1
        else:
            return -1
