class HashTable():
    def __init__(self, capacity=1001):
        self.capacity = capacity
        self.size = 0
        self.data = [[] for _ in range(capacity)]

    def _hash(self, key):
        return sum(bytearray(key)) % self.capacity

    def insert(self, key, value):
        hash_key = self._hash(key)
        self.data[hash_key] = [key, value]

    def lookup(self, key):
        hash_key = self._hash(key)
        ans = self.data[hash_key]
        if ans:
            [found_key, data] = ans
            if key == found_key:
                return data
        return None
