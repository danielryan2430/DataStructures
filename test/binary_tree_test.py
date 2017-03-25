import unittest
from cap1.binary_tree import BinaryTreeNode, BSTStepCounter


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
        self.assertEqual(a, 3)
