# Python Data Structures

This project is meant to show the min, average and maximum possible time for a series of common data structures


# Arguments
|argument|explanation|
|---------|------------|
|-\-data-structure|1: binary tree, 2: HashTable with replacement, 3: Hashtable with chaining, 4: Linkedlist 5. Dynamic Array 6. Skip-list|
|-\-worst-case| defaults to false, will create absolute worst-case scenario for data structure|

#### Worst Case
Certain data structures have worst-case scenarios that depend on the size and order of data.

Here are the following 'worst case' optimizations that are made:
1. Binary Search Tree: In order to create a worst-case scenario for a BST, we sort the data before insertion. This forces the BST to essentially become a linked-list, as every node will be inserted to the right.
2. Hash Table with Chaining: In order to maximize collisions, the worst case scenario for a Hash Table with chaining is to lower its capacity to 1. This will ensure that all items are collisions, and therefore all will be placed in the 'chain' (which is essentially a LinkedList).


# Running

To run the script, simply run the cap1 package.

ex: `python cap1 --data-structure 3`

This command will give you a result in TSV format that will be easily ported to excel or any other tsv editor for analysis and visualization
```
hash_table_with_chaining	lines		25	50	100	200	400	800
hash_table_with_chaining	insert	min	2	2	2	2	2	2
hash_table_with_chaining	insert	avg	2.0	2.0	2.0	2.0	2.0	2.0
hash_table_with_chaining	insert	max	2	2	2	2	2	2

hash_table_with_chaining	lines		25	50	100	200	400	800
hash_table_with_chaining	lookup	min	1	1	1	1	1	1
hash_table_with_chaining	lookup	avg	1.12	1.26	1.47	2.04	2.9375	4.83625
hash_table_with_chaining	lookup	max	3	3	5	7	8	13

hash_table_with_chaining	lines		25	50	100	200	400	800
hash_table_with_chaining	delete	min	1	1	1	1	1	1
hash_table_with_chaining	delete	avg	1.12	1.26	1.47	2.04	2.9375	4.83625
hash_table_with_chaining	delete	max	3	3	5	7	8	13
```
ex with worst-case: `python cap1 --data-structure 3 --worst-case`

```
hash_table_with_chaining	lines		25	50	100	200	400	800
hash_table_with_chaining	insert	min	2	2	2	2	2	2
hash_table_with_chaining	insert	avg	2.0	2.0	2.0	2.0	2.0	2.0
hash_table_with_chaining	insert	max	2	2	2	2	2	2

hash_table_with_chaining	lines		25	50	100	200	400	800
hash_table_with_chaining	lookup	min	1	1	1	1	1	1
hash_table_with_chaining	lookup	avg	13.0	25.5	50.5	100.5	200.5	400.5
hash_table_with_chaining	lookup	max	25	50	100	200	400	800

hash_table_with_chaining	lines		25	50	100	200	400	800
hash_table_with_chaining	delete	min	1	1	1	1	1	1
hash_table_with_chaining	delete	avg	13.0	25.5	50.5	100.5	200.5	400.5
hash_table_with_chaining	delete	max	25	50	100	200	400	800
```