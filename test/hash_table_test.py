import unittest
from cap1.hash_table import HashTable


class TestHashTable(unittest.TestCase):
    def test_insert(self):
        ll = HashTable()
        ll.insert("5","hello")
        self.assertEqual(ll.lookup("5"), "hello")
        self.assertEqual(ll.lookup(4), None)

    # def test_delete(self):
    #     ll = LinkedList()
    #     ll.insert(5)
    #     ll.insert(4)
    #     ll.delete(5)
    #     self.assertEqual(ll.lookup(5), None)
    #     self.assertEqual(ll.lookup(4).value, 4)

