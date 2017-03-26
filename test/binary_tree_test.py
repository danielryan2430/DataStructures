import unittest
from cap1.binary_tree import BinaryTreeNode, BSTStepCounter
import random

class TestBSTStepCounter(unittest.TestCase):
    def test_insert(self):
        bst = BSTStepCounter()
        bst.insert(5)
        self.assertEqual(bst.lookup(5), 1)
        self.assertEqual(bst.lookup(4), -1)

    def test_multi_insert(self):
        bst = BSTStepCounter()
        keys = ['b', 'a', 'd', 'c']
        for i in keys:
            bst.insert(i)

        a = bst.root
        self.assertEqual(a.left.value, 'a')
        self.assertEqual(a.right.value, 'd')
        self.assertEqual(a.right.left.value, 'c')

    def test_multi_insert_count(self):
        bst = BSTStepCounter()
        keys = ['b', 'a', 'd', 'c']
        counts = [bst.insert(i) for i in keys]
        count_dict = dict(zip(keys, counts))
        self.assertEqual(count_dict['b'], 1)
        self.assertEqual(count_dict['a'], 2)
        self.assertEqual(count_dict['d'], 2)
        self.assertEqual(count_dict['c'], 3)

    def test_delete(self):
        bst = BSTStepCounter()
        bst.insert('b')
        bst.insert('a')
        a = bst.delete('b')
        self.assertEqual(bst.lookup('b'), -1)
        self.assertEqual(bst.lookup('a'), 1)
        self.assertEqual(a, 2)

    def test_delete_two_children(self):
        bst = BSTStepCounter()
        bst.insert(5)
        bst.insert(9)
        bst.insert(8)
        bst.insert(10)
        a = bst.delete(9)
        self.assertEqual(bst.root.value, 5)
        self.assertEqual(bst.root.right.value, 10)
        self.assertEqual(bst.root.right.left.value, 8)


    def test_delete_sorted(self):
        bst = BSTStepCounter()
        for i in range(100):
            bst.insert(i)
        for i in range(100):
            a = bst.delete(100 - i - 1)
            self.assertEqual(a > 0, True)

    def test_delete_random(self):
        bst = BSTStepCounter()
        l = [i for i in range(13)]
        print l
        for i in l:
            bst.insert(i)
        # random.shuffle(l)
        j = 0
        for i in l:
            j += 1
            a = bst.delete(i)
            self.assertEqual(a > 0, True)


