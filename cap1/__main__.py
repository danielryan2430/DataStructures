from binary_tree import *

path = 'cap1/data.txt'
f = open(path, 'r')
a = BSTStepCounter()
for i in range(0, 100):
    print len(f.readline())
