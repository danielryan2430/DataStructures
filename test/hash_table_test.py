import unittest
from cap1.hash_table import HashTable
from cap1.hash_table_chaining import HashTableChainingStepCounter


class TestHashTable(unittest.TestCase):
    def test_insert(self):
        ht = HashTable()
        ht.insert("5")
        self.assertEqual(ht.lookup("5"),1)
        self.assertEqual(ht.lookup(4), -1)

    def test_delete(self):
        ht = HashTable()
        ht.insert("5")
        ht.insert("4")

        self.assertEqual(ht.lookup("4"), 1)

        ht.delete("4")

        self.assertEqual(ht.lookup("5"), 1)
        self.assertEqual(ht.lookup("4"), -1)


class TestHashTableWithChaining(unittest.TestCase):
    def test_insert(self):
        ht = HashTableChainingStepCounter()
        keys = ['a', 'b', 'c', 'd', 'e', 'f']
        for i in keys:
            ht.insert(i)
        a = ht.insert('a')
        self.assertEqual(a, 2)
        self.assertEqual(ht.lookup('a'), 1)
        self.assertEqual(ht.lookup('h'), -1)

    def test_delete(self):
        ht = HashTableChainingStepCounter()
        keys = ['a', 'b', 'c', 'd', 'e', 'f']
        for i in keys:
            ht.insert(i)
        ht.delete('c')
        self.assertEqual(ht.lookup('b'), 1)
        self.assertEqual(ht.lookup('a'), 1)
        self.assertEqual(ht.lookup('c'), -1)

    def test_with_collisions(self):
        ht = HashTableChainingStepCounter(capacity=1)
        keys = ['a', 'b', 'c', 'd', 'e', 'f']
        for i in keys:
            ht.insert(i)
        self.assertEqual(ht.lookup('f'), 6)
