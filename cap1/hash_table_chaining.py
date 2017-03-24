from linked_list import LinkedListStepCounter,LinkedListNode



"""
This hashtable h

"""


class HashTableChaining(object):
    def __init__(self, capacity=1001):
        self.capacity = capacity
        self.size = 0
        self.data = [LinkedListStepCounter() for _ in range(capacity)]

    '''

    In order to make chaining significantly more likely, this table's hashing function is purposely high on collisions
    '''
    def _hash(self, key):
        return sum(bytearray(key)) % self.capacity

    def insert(self, value):
        hash_key = self._hash(value)
        return 1 + self.data[hash_key].insert(value)

    def lookup(self, key):
        hash_key = self._hash(key)
        ans = self.data[hash_key].lookup(key)
        if ans != -1:
            return ans + 1
        else:
            return -1

    def delete(self,key):
        hash_key = self._hash(key)
        ans = self.data[hash_key].delete(key)
        if ans != -1:
            return ans + 1
        else:
            return -1