from data_structure import DataStructureBase


class BinaryTreeNode(object):
    def __init__(self, value):
        self._left = None
        self._right = None
        self._value = value
        self.parent = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right = value

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left = value


def _remove_from_parent(node):
    if node.parent:
        if node == node.parent.right:
            node.parent.right = None
        else:
            node.parent.left = None


class BSTStepCounter(DataStructureBase):
    def __init__(self):
        self.root = None

    '''
    _insert:
    :arguments
        - value (String)
    :returns
        - int (num steps to insert)

    inserts value into BST, duplicates will be discarded
    '''

    def insert(self, value):
        if not self.root:
            self.root = BinaryTreeNode(value)
            return 1
        else:
            return self._insert(self.root, BinaryTreeNode(value), 2)

    '''
    _insert:
    :arguments
        - node (BinaryTreeNode)
        - node_to_insert (BinaryTreeNode)
    :returns
        - int (num steps to insert)
    '''

    def _insert(self, node, node_to_insert, count_so_far):
        if node_to_insert.value < node.value:
            if node.left:
                return self._insert(node.left, node_to_insert, count_so_far + 1)
            else:
                node.left = node_to_insert
                node_to_insert.parent = node
                return count_so_far
        elif node_to_insert.value > node.value:
            if node.right:
                return self._insert(node.right, node_to_insert, count_so_far + 1)
            else:
                node.right = node_to_insert
                node_to_insert.parent = node
                return count_so_far

    def lookup(self, value):
        if self.root and self.root.value == value:
            return 1
        return self._lookup(self.root, value, 1)

    '''
    _lookup:
    :arguments
        - node (BinaryTreeNode)
        - value (Any)
    :returns
        - int (num steps to lookup)

    used to recursively find BST node
    '''

    def _lookup(self, node, value, count):
        if not node:
            return -1
        if value < node.value:
            return self._lookup(node.left, value, count + 1)
        elif value > node.value:
            return self._lookup(node.right, value, count + 1)
        else:
            return count

    '''
    delete:
    :arguments
        - value (Any)
    :returns
        - int (num steps to delete)
    used to delete a node in the binary tree
    '''

    def delete(self, value):
        return self._delete(self.root, value, 1)

    '''
    _delete:
    :arguments
        - value (Any)
    :returns
        - int (num steps to delete)
    used to delete a node in the binary tree
    '''

    def _delete(self, node, value, count):
        if not node:
            return -1
        curr = node
        while curr:
            if value < curr.value:
                curr = curr.left
                count += 1
            elif value > curr.value:
                curr = curr.right
                count += 1
            else:
                if curr:
                    return self._delete_node(node, count)
                else:
                    return count
        print "not found"
        return -1

    '''
    _delete_node:
    :arguments
        - node_to_delete (BinaryTreeNode)
        - count (int)
    :returns
        - int (num steps to delete)
    used to delete a node in the binary tree
    '''

    def _delete_node(self, node_to_delete, count):
        c = count
        [successor, successor_count] = self._find_successor(node_to_delete)
        print "successor count {}".format(successor_count)
        c += successor_count
        self._remove_successor_from_parent(successor)

        if successor:
            node_to_delete.value = successor.value
        else:
            node_to_delete = None

        return c

    '''
    _find_min:
    :arguments
        - node (BinaryTreeNode)
    :returns
        - node (
        - int (num steps to find min)
    used to find successor in delete function
    '''

    def _find_min(self, node):
        return self._find_min_with_count(node, 0)

    def _find_min_with_count(self, node, count):
        while node and node.left:
            node = node.left
        return [node, count]

    def _find_successor(self, node):
        if node.right:
            [successor, min_count] = self._find_min(node.right)
        else:
            if node.left:
                successor = node.left
            else:
                successor = node.right
            min_count = 1
        return [successor, min_count]

    def _remove_successor_from_parent(self, successor):
        if successor:
            successor_parent = successor.parent
            if successor == successor_parent.left:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
            if successor.right:
                successor.right.parent = successor.parent
