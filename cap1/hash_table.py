class HashTable(object):
    def __init__(self, capacity=1001):
        self._capacity = capacity
        self._data = [[] for _ in range(capacity)]

    def _hash(self, key):
        return sum(bytearray(key)) % self._capacity

    def insert(self, key, value):
        hash_key = self._hash(key)
        self._data[hash_key] = [key, value]

    def lookup(self, key):
        hash_key = self._hash(key)
        ans = self._data[hash_key]
        if ans:
            [found_key, data] = ans
            if key == found_key:
                return data
        return None

    def delete(self,key):
        hash_key = self._hash(key)
        ans = self._data[hash_key]
        if ans:
            [found_key, _] = ans
            if key == found_key:
                self._data[hash_key] = []
