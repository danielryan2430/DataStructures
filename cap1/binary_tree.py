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


class BSTStepCounter(object):
    def __init__(self):
        self.root = None

    '''
    _insert:
    :arguments
        - value (String)
    :returns
        - int

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
        - int
    '''

    def _insert(self, node, node_to_insert, count_so_far):
        if node_to_insert.value < node.value:
            if node.left:
                return self._insert(node.left, node_to_insert, count_so_far + 1)
            else:
                node.left = node_to_insert
                node_to_insert.parent = node.left
                return count_so_far
        elif node_to_insert.value > node.value:
            if node.right:
                return self._insert(node.right, node_to_insert, count_so_far + 1)
            else:
                node.right = node_to_insert
                node_to_insert.parent = node.right
                return count_so_far

    def lookup(self, value):
        return self._lookup(self.root, value, 1)

    '''
    _lookup:
    :arguments
        - node (BinaryTreeNode)
        - value (Any)
    :returns
        - int

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
        - int
    used to delete a node in the binary tree
    '''

    def delete(self, value):
        return self._delete(value, self.root, 1)

    def _delete(self, value, node, count):
        if not node:
            return -1
        if value < node.value:
            return self._delete(node.left, value, count + 1)
        elif value > node.value:
            return self._delete(node.right, value, count + 1)
        else:
            return self._delete_node(node, count)

    def _delete_node(self, node_to_delete, count):
        c = count
        if node_to_delete.left and node_to_delete.right:
            [successor, min_count] = self._find_min(node_to_delete.right)
            c += min_count
            successor_parent = successor.parent
            if successor == successor_parent.left:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        else:
            if node_to_delete.left:
                successor = node_to_delete.left
            else:
                successor = node_to_delete.right
        node_to_delete.value = successor.value
        del successor
        return c
    '''
    _find_min:
    :arguments
        - node (BinaryTreeNode)
    :returns
        - int

    used to find successor in delete function
    '''

    def _find_min(self, node):
        return self._find_min_with_count(node, 0)

    def _find_min_with_count(self, node, count):
        if node and node.left:
            return self._find_min_with_count(node, count + 1)
        else:
            return [node, count]
