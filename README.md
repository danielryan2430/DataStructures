# Python Data Structures

This project is meant to show the min, average and maximum possible time for a series of common data structures


# Arguments
|argument|explanation|
|---------|------------|
|-\-data-structure|1: binary tree, 2: HashTable with replacement, 3: Hashtable with chaining, 4: Linkedlist|
|-\-worst-case| defaults to false, will create absolute worst-case scenario for data structure|
# Running
`python cap1 --data-structure 3`

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