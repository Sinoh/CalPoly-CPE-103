# Lab 4
[Link](https://www.brinckerhoff.org/clements/2174-csc202/Labs/lab4.html)

For this lab you will implement a binary search tree and explore the implementation of iterators over lists and trees.

Invitation Link

1 Binary Search Tree
For this part of the lab you will implement a binary search tree class that is parameterized on the comes_before operation. More specifically, operations on a binary tree are typically discussed in terms of a "less than" relationship that determines if searching through a tree progress to the left child or the right child. This "less than" relationship is typically realized through the use of the < operator to compare integer values. For this lab you will generalize the tree implementation by using a user provided (at the time of creation) function to determine if one value "comes before" another.

In a file named bst.py , implement the following class and functions.

1.1 To Do
Define a BinarySearchTree class with an appropriate __init__ function that takes, as an argument, the comes_before function discussed above.

Define each of the following functions.

is_empty — given a BinarySearchTree, return True if the tree is empty, False otherwise.

insert — given a BinarySearchTree and a value as arguments, insert adds the value to the tree by using the comes_before function to determine which path to take at each node; inserts into the left subtree if the value "comes before" the value stored in the current node and into the right subtree otherwise.

This function returns the resulting tree.

lookup — given a BinarySearchTree and a value as arguments, lookup returns True if the value is stored in the tree and False otherwise. Note, however, that the tree was not created with an equality comparison function. Instead, you will use the comes_before function to determine if the value appears in the tree. More specifically, when comparing two values, if neither value "comes before" the other, then the values will be considered equal (i.e., for our purposes, (not (a < b) and not (b < a)) -> a = b).

delete — given a BinarySearchTree and a value as arguments, delete removes the value from the tree (if present) while preserving the binary search tree property that, for a given node’s value, the values in the left subtree come before and the values in the right subtree do not. If the tree happens to have multiple nodes containing the value to be removed, only a single such node will be removed.

This function returns the resulting tree.

1.1.1 Test Cases
In a file named bst_tests.py , write test cases to verify that your implementation works correctly for various comes_before functions.

2 Iterator Object
An iterator allows access to the elements in a collection in a sequential manner. Iterators are particularly useful for generalizing functionality over all elements of a data structure without concern for the specific type of data structure (i.e., when writing a function that must process all elements without regard for how they are stored). Iterators are also useful when working with data structures that do not support direct access to their elements (i.e., such as a linked list, where a get operation, for instance, would start traversing from the beginning of the list on each call).

One common approach to implementing an interator is to use an object to track the position within the associated data structure and to provide operations to check if there are more elements and, if there are, to access the next element.

2.1 To Do
Copy your linked_list.py file from the previous lab. Add the following class and functions.

Define an Iterator class to track the position of the iterator within the associated linked list (passed as the only argument to __init__).

Define a function, object_iterator, that takes a linked list and returns an Iterator object.

Define the has_next function that takes an Iterator object and returns True if there is another value to return from the iterated list.

Define the get_next function that takes an Iterator object and returns the next value in the iteration sequence; if there are no remaining values, a StopIteration exception should be raised.

2.1.1 Test Cases
In a file named object_iterator_tests.py , write test cases to verify that your implementation works correctly for various linked lists, including tests of attempts to iterate beyond the end of the list.

3 yield
Python supports a yield statement to, roughly, provide a "return" value by suspending a function invocation (a function call). Execution of the suspended function will continue after the

yield when another result is requested from the function. This is done, for instance, by iterating through the yielded values in a for statement.

For instance, in the following example, the seven_nine

function will yield the value 7 first and then yield the value 9 if another result is needed. The for statement consumes these values. You should run this code in the interpreter and modify it to yield additional values to make sure the functionality is clear. What is the result of a simple function call to seven_nine ? (It turns out that it is very similar to what you just implemented in the previous part of this lab. See Further Details

below.)

 

def seven_nine():

   yield 7

   yield 9

 

for value in seven_nine():

   print(value)

 

In your linked_list.py file, add the following function.

3.1 To Do
Define a function, yield_iterator , to take a linked list as an argument and to yield each value within the list. Since we are using Python 3, you can use yield from when making the recursive call in order to yield the element that is yielded within the recursive call.

3.1.1 Test Cases
In a file named yield_iterator_tests.py , write test cases to verify that your implementation works correctly for various linked lists.

3.1.2 Further Details
More accurately, in Python, the use of yield creates what is called a generator. Generators support an operation to retrieve the next generated value; it is this operation that triggers the initial execution of the function code and each subsequent execution following a yield . This can be seen more explicitly if you run the following code (and, thus, makes more apparent the similarities between this implementation and that of the earlier part of this lab).

 

def seven_nine():

   yield 7

   yield 9

 

sn = seven_nine()

type(sn)

 

next(sn)

next(sn)

next(sn)

 

4 Tree Traversal Strategies
It is often desirable to access every element of a tree for further processing. For instance, one might wish to print every element, to write every element to a file, to insert every element into a database, or to perform some computation on every element. A tree traversal strategy specifies the order in which the nodes of a tree are visited, where "visited" in this case amounts to processing of the data stored within the node.

Instead of writing a separate function for each traversal task (i.e., for printing, for inserting into a database, etc.), we will hide the traversal steps behind an iterator that provides access to the values within the tree. Doing this will allow the user of your iterator to process the data as they wish without concern for explicitly traversing (walking) the tree.

More specifically, you will use Python’s yield statement to define a generator. This allows you to write your generator code in a manner very similar to a recursive depth-first traversal without concern for "going back up" the tree. (Consider, after lab, how you might implement this using an explicit iterator object; what data needs to be tracked?)

Note, carefully, that each recursive call will also be returning an iterator (a generator). Since we are using Python 3, you can use

yield from when making the recursive call to yield, in turn, each element of the generator (prior to Python 3, one would need to consume and yield each element from that generator in a loop).

4.1 To Do
Define each of the following functions in your bst.py file.

prefix_iterator — given a BinarySearchTree, returns an iterator (using yield) of the elements in prefix order wherein, for a given node, the node is visited before its children (visit the left child before the right child).

infix_iterator — given a BinarySearchTree, returns an iterator (using yield) of the elements in infix order wherein, for a given node, the node is visited after its left child but before its right child.

postfix_iterator — given a BinarySearchTree, returns an iterator (using yield) of the elements in postfix order wherein, for a given node, the node is visited before its children.

4.1.1 Test Cases
In a file named bst_iterator_tests.py , write test cases to verify that your iterators work correctly for various trees.

5 Lab Credit
You must submit your files for grading to receive credit for this lab. This requires that you use the specified file names (listed below) and the specified function names for the required operations (review the lab description to verify that these match).

Recall that the file names are as follows.

bst.py – binary search tree implementation

bst_tests.py – binary search tree tests

linked_list.py – updated linked list implementation

object_iterator_tests.py – object iterator tests

yield_iterator_tests.py – yield iterator tests

bst_iterator_tests.py – tree traversal strategy tests