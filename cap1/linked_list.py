class LinkedListNode():
    def __init__(self, value):
        self._next = None
        self._value = value


    @property
    def value(self):
        return self._value

    @property
    def next(self):
        return self._next

    def set_next(self, next):
        self._next = next


class LinkedList(object):
    def __init__(self):
        self._head = None
        self._last = None

    def printAll(self):
        curr = self._head
        while curr:
            print curr.value
            curr = curr.next

    def insert(self, value):
        node = LinkedListNode(value)
        if not self._head:
            self._head = node
            self._last = node
        else:
            self._last.set_next(node)
            self._last = node

    def lookup(self, value):
        current = self._head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        prev = None
        current = self._head
        while current:
            if current.value == value:
                print "found value"
                break
            prev = current
            current = current.next

        # if there is no previous, then we're at the head of the list
        if prev:
            prev.next = current.next
        else:
            self._head = current.next
