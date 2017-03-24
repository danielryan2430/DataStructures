from binary_tree import *
from linked_list import *
from datastructure_analyzer import *

path = 'cap1/data.txt'
f = open(path, 'r')
a = LinkedListStepCounter()
lines = [next(f) for x in range(100)]
b = BigOAnalyzer(a)

b.test_lookup(lines)


