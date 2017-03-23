import unittest
from cap1.hash_table import HashTable
from cap1.hash_table_chaining import HashTableChaining


class TestHashTable(unittest.TestCase):
    def test_insert(self):
        ht = HashTable()
        ht.insert("5","hello")
        self.assertEqual(ht.lookup("5"), "hello")
        self.assertEqual(ht.lookup(4), None)

    def test_delete(self):
        ht = HashTable()
        ht.insert("5", "hello")
        ht.insert("4", "goodbye")

        self.assertEqual(ht.lookup("4"), "goodbye")

        ht.delete("4")

        self.assertEqual(ht.lookup("5"), "hello")
        self.assertEqual(ht.lookup("4"), None)


class TestHashTableWithChaining(unittest.TestCase):
    def test_insert(self):
        ht = HashTableChaining()
        ht.insert("hello")
        self.assertEqual(ht.lookup("hello"), "hello")
        self.assertEqual(ht.lookup(4), None)

    def test_delete(self):
        ht = HashTableChaining()
        ht.insert("hello")
        ht.insert("goodbye")
        self.assertEqual(ht.lookup("goodbye"), "goodbye")
        ht.delete("goodbye")

        self.assertEqual(ht.lookup("hello"), "hello")
        self.assertEqual(ht.lookup("goodbye"), None)