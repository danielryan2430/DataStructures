import unittest
from cap1.linked_list import LinkedListStepCounter


class TestLinkedList(unittest.TestCase):
    def test_insert(self):
        ll = LinkedListStepCounter()
        ll.insert(5)
        ll.insert(4)
        ll.insert(3)

        self.assertEqual(ll.lookup(5), 1)
        self.assertEqual(ll.lookup(4), 2)
        self.assertEqual(ll.lookup(3), 3)
        self.assertEqual(ll.lookup(2), -1)

    def test_delete(self):
        ll = LinkedListStepCounter()
        ll.insert(5)
        ll.insert(4)
        ll.delete(5)
        self.assertEqual(ll.lookup(5), -1)
        self.assertEqual(ll.lookup(4), 1)

    def test_delete_mid(self):
        ll = LinkedListStepCounter()
        ll.insert(5)
        ll.insert(4)
        ll.insert(3)
        del_count = ll.delete(4)
        self.assertEqual(del_count, 2)
        self.assertEqual(ll.lookup(5), 1)
        self.assertEqual(ll.lookup(4), -1)
        self.assertEqual(ll.lookup(3), 2)


