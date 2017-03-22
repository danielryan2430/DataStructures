import unittest
from cap1.binary_tree import BinaryTreeNode,BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(5)
        self.assertEqual(bst.lookup(5).value, 5)
        self.assertEqual(bst.lookup(4), None)

    def test_delete(self):
        bst = BinarySearchTree()
        bst.insert(5)
        bst.insert(4)
        bst.delete(5)
        self.assertEqual(bst.lookup(5), None)
        self.assertEqual(bst.lookup(4).value, 4)
