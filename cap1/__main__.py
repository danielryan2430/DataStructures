from binary_tree import *
from linked_list import *
from datastructure_analyzer import *
from hash_table_chaining import *
from hash_table import *
import argparse


parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--data-structure', default=0,
                    help='which data structure to use\n'
                         '1: BST\n'
                         '2: Hastable\n'
                         '3: Hashtable with chaining\n'
                         '4: LinkedList')
parser.add_argument('--worst-case', default=False, help='whether to specifically test the worst-possible case for DS')


def find_ds(ds_input):
    if ds_input == 1:
        ds_tmp = BSTStepCounter()
    elif ds_input == 2:
        ds_tmp = HashTable()
    elif ds_input == 3:
        ds_tmp = HashTableChainingStepCounter()
    elif ds_input == 4:
        ds_tmp = LinkedListStepCounter()
    else:
        raise Exception('invalid input')
    return ds_tmp

args = parser.parse_args()
print args.worst_case
ds_num = args.data_structure



path = 'cap1/data.txt'

f = open(path, 'r')
lines = []
for x in range(900):
    lines.append(f.readline())

i = 100
while i <= 800:
    ds = find_ds(int(ds_num))
    curr_lines = []
    for x in range(i):
        curr_lines.append(lines[x])

    # list.sort(lines)
    b = BigOAnalyzer(ds)
    b.test_insert(curr_lines)
    i *= 2
    f.close()

i = 100

while i <= 800:
    ds = find_ds(int(ds_num))
    curr_lines = []
    for x in range(i):
        curr_lines.append(lines[i])
    for x in lines:
        ds.insert(x)
    # list.sort(lines)
    b = BigOAnalyzer(ds)
    b.test_lookup(curr_lines)
    i *= 2

f.close()
i = 100

while i <= 800:
    ds = find_ds(int(ds_num))
    curr_lines = []
    for x in range(i):
        curr_lines.append(lines[x])
    for x in curr_lines:
        ds.insert(x)
    # list.sort(lines)
    b = BigOAnalyzer(ds)
    curr_lines = list(reversed(curr_lines))
    b.test_delete(curr_lines)
    i *= 2


