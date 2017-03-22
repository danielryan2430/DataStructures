class LinkedListNode():
    def __init__(self, value):
        self.next = None
        self.value = value\

    def set_next(self, next):
        self.next = next


class LinkedList():
    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, value):
        node = LinkedListNode(value)
        if not self.head:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def lookup(self,value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                self._remove_node(current)
                break
            current = current.next

    def _remove_node(self,node):
        if node.next:
            node.value = node.next.value
            n = node.next
            node.next = node.next.next
            del n
        else:
            del node
