# Lab 2

[Link](https://www.brinckerhoff.org/clements/2174-csc202/Labs/lab2.html)

To solve a problem, one often considers different ways to represent the relevant data. In some instances, the data might reasonably be placed in a sequence or the data might naturally dictate a hierarchy. This lab introduces the basic structure of and operations on two of the most common data structures: a linked list and a binary tree.

Here’s the invitation link for this lab’s repo:

Invitation

## 1 - Linked List
A linked list is either
- Empty; or
- A pair containing some value and the rest of the list

One realization of this definition in Python is the following class to represent pairs and, for instance, the use of "mt" to represent Empty (because we need something to stand for nothing).
```
class Pair:
   def __init__(self, value, rest):
      self.value = value
      self.rest = rest
    # boilerplate omitted
```
One can use instances of this class to create a list of the numbers **7** ,**4** ,**2** ,**19** ,**42** (in this order) as follows.

**Pair(7, Pair(4, Pair(2, Pair(19, Pair(42, "mt")))))**

This explicit form is useful at this point to emphasize the structure of the data. Working with longer lists, say of millions of elements, will require building a list incrementally, and we will get there.
### 1.1 - Operations
In the file named "list_ops.py", write a data definition for a NumList, as we did in class.

Next, follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design the following functions. Your test cases must use the unittest module; place your test cases in a single TestCase class at the bottom of the file

Note: Your goal is not to just implement these operations so that they pass some test cases. Pay particular attention to the structure of the data, the similarities between the functions that you are writing, and how the code is structured in a manner similar to the data (especially when written recursively, and even more so for binary trees).

Finally, none of these functions require value mutation. Don’t use value mutation to solve any of these problems.

length: Define a function named length that takes a linked list and returns the number of values in the list.

sum Define a function named sum that takes a linked list of numeric values and returns the sum of the values in the list.

count_greater_than Define a function named count_greater_than that takes a linked list and a threshold value, and that returns the number of values in the list strictly greater than the threshold (e.g., the number of values in the sample list above that are greater than 10).

find Define a function named find that takes a linked list and a value to find, and that returns the position within the list where the given value appears (where the first value in a non-empty list is at position 0). If the given value does not appear in the list, return None. (Hint: this function is easier with an accumulator.)

sub_one_map Define a function named sub_one_map that takes a linked list, and returns a new linked list where each number is smaller by one.

insert Define a function named insert that accepts a NumList in ascending, sorted order and a new number, and returns a new list containing the new number in the proper location.

## 2 - Binary Tree
A binary tree is either
Empty; or

A node containing some value, a left subtree, and a right subtree

One realization of this definition in Python is the following class to represent tree nodes and, again, the use of "mt" to represent empty.
[!Test](https://www.brinckerhoff.org/clements/2174-csc202/Labs/pict.png "Title")

```
class TreeNode:
   def __init__(self, value, left, right):
      self.value = value
      self.left = left
      self.right = right
   # boilerplate omitted
```
One can use instances of this class to create the pictured tree as follows.
image

TreeNode(4,

   TreeNode(9,

      TreeNode(19, "mt", "mt"),

      TreeNode(2, TreeNode(103, "mt", "mt"), "mt")

   ),

   TreeNode(42, "mt", TreeNode(7, "mt", "mt"))

)

This explicit form is useful at this point to emphasize the structure of the data. Working with larger trees, say of millions of elements, will require building the tree incrementally (and defining how/where elements are added to the tree); as with lists, we will get there.

### 2.1 - Operations
In a file named tree_ops.py, develop the class definition for a binary tree of numbers, add it to the appropriate section, and implement each of the following operations. Follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design these functions. Your test cases must use the unittest module; place your test cases in a single TestCase class at the bottom of the file.
size Define a function named size that takes a binary tree and returns the number of the elements in the tree.

num_leaves Define a function named num_leaves that takes a binary tree and returns the number of the leaves (i.e., those nodes with both subtrees empty) in the tree.

sum Define a function named sum that takes a binary tree of numeric values and returns the sum of the values in the tree.

height Skip this function! Freebie! Go get a lemonade.

has_triple Define a function named has_triple that returns true exactly when a tree node (anywhere in the tree) with value n contains an immediate child node with value 3n.

sub_one_map Define a function named sub_one_map that returns a new tree where each value is smaller by one. Yes, this is just like the list function.

## 3 - Lab Credit
You must submit your files for grading to receive credit for this lab. This requires that you use the specified file names (listed below) and the specified function names for the required operations (review the lab description to verify that these match).

Recall that the file names are as follows.
- "list_ops.py" – linked list operations

- "tree_ops.py" – binary tree operations
