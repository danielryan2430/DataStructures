from data_structure import DataStructureBase


class ArrayList(DataStructureBase):
    @property
    def name(self):
        return "array_list"

    def __init__(self, capacity, amortized):
        self._size = 0
        self._capacity = capacity
        self._data = []
        self._amortized = amortized
        self.increase_capacity()

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    '''
    increase_capacity
    :arguments
        - None
    :returns
        - int (num steps to increase capacity (or 1 if amortized))
    when the threshold is met, this allows us to resize the arraylist
    '''

    def increase_capacity(self):
        new_slots = []
        count = 0
        for i in range(self.capacity):
            if not self._amortized:
                count += 1
            new_slots.append('')
        self._data.extend(new_slots)
        return count

    '''
    insert
    :arguments
        - value(string)
    :returns
        - int (num steps to insert)
    insert value
    '''

    def insert(self, value):
        count = 1
        if self.size % self.capacity == 0:
            count += self.increase_capacity()
        self._data[self.size] = value
        self._size += 1
        return count

    '''
    lookup
    :arguments
        - value(string)
    :returns
        - int (num steps to lookup)
    lookup value
    '''
    def lookup(self, value):
        count = 1
        curr = 0
        while curr < self.size:
            if self._data[curr] == value:
                return count
            count += 1
            curr += 1
        return -1

    '''
    delete
    :arguments
        - value(string)
    :returns
        - int (num steps to delete)
    delete value
    '''
    def delete(self, value):
        count = 1
        curr = 0
        found = False
        while curr < self.size:
            if self._data[curr] == value:
                found = True
                break
            curr += 1
            count += 1
        if found:
            while curr < self.size:
                count += 1
                self._data[curr] = self._data[curr + 1]
                curr += 1
            self._data[curr] = []
            self._size -= 1
        return count
