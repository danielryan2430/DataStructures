import unittest
from cap1.skip_list import SkipList


class SkipListTest(unittest.TestCase):
    def test_insert(self):
        a = SkipList()
        for i in range(100):
            a.insert(str(i))
        for i in range(100):
            self.assertEqual(a.lookup(str(i)) > 0, True)

    def test_insert_and_delete(self):
        a = SkipList()
        for i in range(100):
            a.insert(str(i))
        for i in range(100):
            #all values should exist before deletion, and should not exist after deletion
            self.assertEqual(a.lookup(str(i)) > 0, True)
            self.assertEqual(a.delete(str(i)) > 0, True)
            self.assertEqual(a.lookup(str(i)) > 0, False)