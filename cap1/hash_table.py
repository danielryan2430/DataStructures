class HashTable(object):
    def __init__(self, capacity=1001):
        self._capacity = capacity
        self._data = [[] for _ in range(capacity)]

    def _hash(self, key):
        return sum(bytearray(key)) % self._capacity

    def insert(self, value):
        hash_key = self._hash(value)
        self._data[hash_key] = value

    def lookup(self, key):
        hash_key = self._hash(key)
        ans = self._data[hash_key]

        if ans == key:
            return 1
        return -1

    def delete(self, key):
        hash_key = self._hash(key)
        ans = self._data[hash_key]
        if ans == key:
            self._data[hash_key] = []
            return 1
        return -1
