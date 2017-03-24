from data_structure import DataStructureBase


class LinkedListNode(object):
    def __init__(self, value):
        self._next = None
        self._value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self,value):
        self._value = value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value):
        self._next = value


class LinkedListStepCounter(DataStructureBase):
    def __init__(self):
        self._head = None
        self._last = None

    def print_all(self):
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
            self._last.next = node
            self._last = node
        return 1

    def lookup(self, value):
        current = self._head
        i = 1
        while current:
            if current.value == value:
                return i
            current = current.next
            i += 1
        return -1

    def delete(self, value):
        prev = None
        current = self._head
        found = False
        i = 1
        while current:
            if current.value == value:
                found = True
                break
            prev = current
            current = current.next
            i += 1

        # if there is no previous, then we're at the head of the list
        if found:
            if prev:
                prev.next = current.next
            else:
                self._head = current.next
            return i
        else:
            return -1
