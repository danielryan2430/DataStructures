class LinkedListNode():
    def __init__(self, value):
        self.next = None
        self.value = value \
 \
    def set_next(self, next):
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.last = None

    def printAll(self):
        curr = self.head
        while curr:
            print curr.value
            curr = curr.next

    def insert(self, value):
        node = LinkedListNode(value)
        if not self.head:
            self.head = node
            self.last = node
        else:
            self.last.next = node
            self.last = node

    def lookup(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def delete(self, value):
        prev = None
        current = self.head
        while current:
            if current.value == value:
                print "found value"
                break
            current = current.next

        # if there is no previous, then we're at the head of the list
        if prev:
            prev.next = current.next
        else:
            self.head = current.next