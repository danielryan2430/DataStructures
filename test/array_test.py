import unittest
import random
from cap1.array import ArrayList


class TestArrayList(unittest.TestCase):
    def test_insert(self):
        bst = ArrayList(10, False)
        for i in range(100):
            bst.insert(str(i))
        for i in range(100):
            self.assertEqual(bst.get(i), str(i))

    def test_lookup(self):
        bst = ArrayList(10, False)
        for i in range(100):
            bst.insert(str(i))
        for i in range(100):
            self.assertEqual(bst.lookup(str(i)), i+1)

    def test_delete(self):
        bst = ArrayList(10, False)
        for i in range(100):
            bst.insert(str(i))

        random_delete = [str(i) for i in range(100)]
        random.shuffle(random_delete)
        size = 99
        for i in random_delete:
            # assert all values are in the array
            self.assertEqual(bst.delete(i) > 0, True)
            self.assertEqual(bst.size, size)
            size -= 1
