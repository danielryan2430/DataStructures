from binary_tree import *
from linked_list import *
from skip_list import *
from array import *
from datastructure_analyzer import *
from hash_table_chaining import *
from hash_table import *
import argparse
import random

parser = argparse.ArgumentParser(description='Process Big O of data structures.')
parser.add_argument('--data-structure', default=0,
                    help='which data structure to use\n'
                         '1: BST\n'
                         '2: Hastable\n'
                         '3: Hashtable with chaining\n'
                         '4: LinkedList')
parser.add_argument('--worst-case', default=False, action='store_true',
                    help='whether to specifically test the worst-possible case for DS')

parser.add_argument('--amortized', default=False, action='store_true',
                    help='whether to assume amortized Big O')


def to_csv_line(otype, ftype, atype, input):
    a = [otype, ftype, atype]
    a.extend(input)
    return '\t'.join(str(e) for e in a)


def print_list(otype, ftype, ans):
    min_val = [l[0] for l in ans]
    avg_val = [l[1] for l in ans]
    max_val = [l[2] for l in ans]
    num_lines = [l[3] for l in ans]

    print ""
    print to_csv_line(otype, 'lines', '', num_lines)
    print to_csv_line(otype, ftype, 'min', min_val)
    print to_csv_line(otype, ftype, 'avg', avg_val)
    print to_csv_line(otype, ftype, 'max', max_val)


args = parser.parse_args()


def find_ds(ds_input):
    if ds_input == 1:
        ds_tmp = BSTStepCounter()
    elif ds_input == 2:
        ds_tmp = HashTable()
    elif ds_input == 3:
        if args.worst_case:
            ds_tmp = HashTableChainingStepCounter(1)
        else:
            ds_tmp = HashTableChainingStepCounter(1001)
    elif ds_input == 4:
        ds_tmp = LinkedListStepCounter()
    elif ds_input == 5:
        ds_tmp = ArrayList(100, args.amortized)
    elif ds_input == 6:
        if args.worst_case:
            ds_tmp = SkipList(max_levels=0)
        else:
            ds_tmp = SkipList()
    else:
        raise Exception('invalid input')
    return ds_tmp


ds_num = args.data_structure

path = 'cap1/data.txt'

f = open(path, 'r')
lines = []
for x in range(900):
    lines.append(f.readline())
f.close()

if args.worst_case:
    lines = sorted(lines)

initial_lines = 25
max_lines = 800


def gather_data_for_insert():
    i = initial_lines
    res_list = []
    while i <= max_lines:
        ds = find_ds(int(ds_num))
        curr_lines = lines[:i]
        b = BigOAnalyzer(ds)
        res_list.append(b.test_insert(curr_lines))
        i *= 2
    print_list(ds.name, 'insert', res_list)


def gather_data_for_lookup():
    i = initial_lines
    res_list = []
    while i <= max_lines:
        ds = find_ds(int(ds_num))
        curr_lines = lines[:i]
        for x in lines:
            ds.insert(x)
        b = BigOAnalyzer(ds)
        if args.worst_case:
            curr_lines = list(reversed(curr_lines))
        else:
            random.shuffle(curr_lines)
        res_list.append(b.test_lookup(curr_lines))
        i *= 2
    print_list(ds.name, 'lookup', res_list)


def gather_data_for_delete():
    i = initial_lines
    res_list = []
    while i <= max_lines:
        ds = find_ds(int(ds_num))
        curr_lines = lines[:i]
        for x in curr_lines:
            ds.insert(x)
        b = BigOAnalyzer(ds)
        if args.worst_case:
            curr_lines = list(reversed(curr_lines))
        else:
            random.shuffle(curr_lines)
        res_list.append(b.test_delete(curr_lines))
        i *= 2
    print_list(ds.name, 'delete', res_list)

gather_data_for_insert()
gather_data_for_lookup()
gather_data_for_delete()
