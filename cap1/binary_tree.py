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
            # print "returning 1"
            return 1
        else:
            a = self._insert(self.root, BinaryTreeNode(value), 2)
            # print "returning {}".format(a)
            return a

    '''
    _insert:
    :arguments
        - node (BinaryTreeNode)
        - node_to_insert (BinaryTreeNode)
    :returns
        - int (num steps to insert)
    '''

    def _insert(self, node, node_to_insert, count_so_far):
        curr = node
        while curr:
            if node_to_insert.value < curr.value:
                if curr.left:
                    curr = curr.left
                    count_so_far +=1
                else:
                    curr.left = node_to_insert
                    node_to_insert.parent = curr
                    return count_so_far
            elif node_to_insert.value > curr.value:
                if curr.right:
                    curr = curr.right
                    count_so_far += 1
                else:
                    curr.right = node_to_insert
                    node_to_insert.parent = curr
                    return count_so_far
        return -1

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
        curr = node
        while curr:
            if value < curr.value:
                curr = curr.left
                count += 1
            elif value > curr.value:
                curr = curr.right
                count += 1
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
                    return self._delete_node(curr, count)
                else:
                    return count
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
        c += successor_count
        self._remove_successor_from_parent(successor)
        self._replace_node_with_successor(node_to_delete, successor)

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
                successor.right.parent = successor_parent

    def _replace_node_with_successor(self, node, repl):
        if repl:
            repl.parent = node.parent
        if node.parent and node == node.parent.left:
            node.parent.left = repl
        elif node.parent and node == node.parent.right:
            node.parent.right = repl
        else:
            self.root = repl



