import unittest
from cap1.binary_tree import BinaryTreeNode,BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):
    def test_insert(self):
        bst = BinarySearchTree()
        bst.insert(5)
        self.assertEqual(bst.lookup(5).value, 5)
        self.assertEqual(bst.lookup(4), None)

    def test_multi_insert(self):
        bst = BinarySearchTree()
        bst.insert('b')
        bst.insert('a')
        bst.insert('d')
        bst.insert('c')

        a = bst.lookup('b')
        self.assertEqual(a.left.value, 'a')
        self.assertEqual(a.right.value, 'd')
        self.assertEqual(a.right.left.value, 'c')

    def test_delete(self):
        bst = BinarySearchTree()
        bst.insert('b')
        bst.insert('a')
        bst.delete('b')
        self.assertEqual(bst.lookup('b'), None)
        self.assertEqual(bst.lookup('a').value, 'a')
