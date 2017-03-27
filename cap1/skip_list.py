from data_structure import DataStructureBase
import random


class SkipListNode(object):
    def __init__(self, value, down=None):
        self._value = value
        self._right = None
        self._down = down

    @property
    def value(self):
        return self._value

    @property
    def down(self):
        return self._down

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, right):
        self._right = right

    @down.setter
    def down(self, down):
        self._down = down


def flip_coin():
    return random.randrange(0, 2)


class SkipList(DataStructureBase):
    """
    SkipList:

    A skiplist is a probabilistic data structure that uses probabilities to maintain a sorted list that performs
    (theta) log(n) for insert, lookup, and delete. Nodes are randomly promoted to higher "levels" to create "fast-lanes"
    in searches. Probabilities are used since the resulting size of the data is not pre-determined.

    """
    @property
    def name(self):
        return "skip_list"

    def __init__(self, max_levels= 10000):
        self._head = SkipListNode(None)
        self._lists = [SkipListNode(None)]
        self._max_levels = max_levels
        self._height = 0

    def _find_level_for_entry(self):
        """

        :return: int

        continually "flips coin" to decide what level a value should end up in.
        """
        height = 0
        for i in range(self._height):
            if flip_coin() == 1:
                height += 1
            else:
                break
        return height

    def _add_level(self):
        if self._height < self._max_levels:
            self._height += 1
            self._lists.append(SkipListNode(None, down=self._lists[self._height - 1]))

    @staticmethod
    def _find_prev_node_for_level(start, value):
        """

        :param start:
        :param value:
        :return:

        finds value in current level that is < the inserted value.
        Rather than beginning at the beginning of the line, this function can take advantage of
        existing traversal, allowing for log(n) lookup
        """
        curr = start
        count = 0
        while curr.right and curr.right.value < value:
            curr = curr.right
            count += 1
        return [curr, count]

    @staticmethod
    def _insert_right(prev, value):
        node = SkipListNode(value)
        node.right = prev.right
        prev.right = node

    @staticmethod
    def _delete_right(prev):
        prev.right = prev.right.right

    def insert(self, value):
        """

        :param value: string
        insert a value into the skip-list
        function will used existing skips to insert in ~log(n) time.
        """
        level = self._find_level_for_entry()
        # if we've reached the current top level, we should add an extra level
        if level == self._height:
            self._add_level()
        curr_level = self._height
        [prev, count] = self._find_prev_node_for_level(self._lists[curr_level], value)
        prev_inserted_node = None
        while curr_level >= 0:
            [prev, prev_count] = self._find_prev_node_for_level(prev, value)
            count += prev_count
            if curr_level <= level:
                self._insert_right(prev, value)
                inserted_node = prev.right
                if prev_inserted_node:
                    prev_inserted_node.down = inserted_node
                prev_inserted_node = inserted_node
            prev = prev.down
            curr_level -= 1
        return count

    def lookup(self, value):
        """

        :param value: string
        :return: int

        performs a skip-list lookup. Will traverse lists taking advantage of previous level's  traversal.
        Performs in log(n) time.
        """
        curr_level = self._height
        curr_node = self._lists[self._height]
        count = 0
        while curr_level >= 0:
            [curr_node, prev_count] = self._find_prev_node_for_level(curr_node, value)
            count += prev_count
            if curr_node.right and curr_node.right.value == value:
                return count
            elif curr_node.right and curr_node.right.value < value:
                curr_node = curr_node.right
            else:
                curr_level -= 1
                count += 1
                curr_node = curr_node.down
        return -1

    def delete(self,value):
        """

        :param value: string
        :return: int

        performs a skip-list deletion. Will traverse lists taking advantage of previous level's traversal.
        Performs in log(n) time.
        """
        curr_level = self._height
        curr_node = self._lists[self._height]
        count = 0
        while curr_level >= 0:
            [curr_node, prev_count] = self._find_prev_node_for_level(curr_node, value)
            count += prev_count
            if curr_node.right and curr_node.right.value == value:
                self._delete_right(curr_node)
            elif curr_node.right and curr_node.right.value < value:
                curr_node = curr_node.right
            else:
                curr_level -= 1
                count += 1
                curr_node = curr_node.down
        return count
