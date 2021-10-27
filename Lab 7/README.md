# Lab 7
For this lab you will explore one implementation of a hash table with a separate chaining collision resolution strategy.

[Link](https://www.brinckerhoff.org/clements/2174-csc202/Labs/lab7.html)

1 Hash Table
In order to insert an item into a hash table, the item must have a unique key associated with it. Recall that the key can be part of the item itself, or it can be separate from the item being inserted into the hash table. In our implementation, the key will be separate from the item.

1.1 To Do
In this implementation, each location in the hash table is represented by a list. To represent this list, you may use any list implementation, including your link-based or array-based list implementations, and the built-in python list.

Write your hash table implementation in a file named hash_table_chaining.py with tests in hash_table_chaining_tests.py.

Define each of the following functions. As always, follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design each of these functions.

empty_hash_table—this function takes no parameters and returns an empty hash table with an initial size of 8.

insert—this function takes a hash table, a key, and an item. The function will insert both the item and the key into the hash table based on the built-in python hash value of the key. If the key-value pair being inserted into the hash table is a duplicate key, the old key-value pair will be replaced by the new key-value pair. If the insert causes the load factor of the hash table to become greater than 1.5, the size of the hash table will be doubled, and the hash table will be rehashed. The function returns the resulting hash table.

get—this function takes a hash table and a key and returns the item from the hash table associated with the key. If no key-value pair is associated with the key, the function raises a LookupError exception.

remove—this function takes a hash table and a key, removes the key-value pair from the hash table, andreturns the resulting hash table. If no key-value pair is associated with the key, the function raises a LookupError exception.

size—this function takes a hash table and returns the number of items in the hash table.

load_factor—this function takes a hash table and returns the current load factor of the hash table.

collisions—this function takes a hash table and returns the number of collisions that have occured during insertions into the hash table. A collision occurs when an item is inserted into the hash table at a location where one or more key-value pairs has alredy been inserted.

1.2 Lab Credit
You must submit your files for grading to receive credit for this lab. This requires that you use the specified file names (listed below) and the specified function names for the required operations (review the lab description to verify that these match).

Recall that the file names are as follows.

hash_table_chaining.py

hash_table_chaining_tests.py

You must submit any other files required by your implementaion or test files.