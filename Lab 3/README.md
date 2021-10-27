# Lab 3

[Link](https://www.brinckerhoff.org/clements/2174-csc202/Labs/lab3.html)


This lab provides an introduction to list implementations. In particular, you are asked to implement both a linked list and an "array" list.

Here’s the invitation link to create a repository for this lab.

1 List Abstract Data Type
The operations supported by a list can be discussed independent of the implementation. As such, a given list implementation can be used through the set of operations without programmatic concern for the details of the implementation. This allows one to vary the implementation based on the characteristics of the problem being solved.

Details of each operation are given below; you will implement these operations for a linked list implementation and for an "array" list implementation. You must verify, via test cases, that your implementations behave as expected (i.e., that they "work"). In a separate project, you will perform an empirical study of the performance characteristics of these two implementations.

empty_list This function takes no arguments and returns an empty list.

add This function takes a list, an integer index, and another value (of any type) as arguments and places the value at index position in the list (zero-based indexing; any element at the given index before this operation will now immediately follow the new element). If the index is invalid (i.e., less than 0 or greater than the current length), then this operation should raise an IndexError exception. (Note that an index equal to the length is allowed and results in the new value being added to the end of the list.)

This function must return the resulting list.

length This function takes a list as an argument and returns the number of elements currently in the list.

get This function takes a list and an integer index as arguments and returns the value at the index position in the list (zero-based indexing). If the index is invalid (i.e., it falls outside the bounds of the list), then this operation should raise an IndexError exception.

set This function takes a list, an integer index, and another value (of any type) as arguments and replaces the element at index position in the list with the given value. If the index is invalid, then this operation should raise an IndexError exception.

This function must return the resulting list.

remove This function takes a list and an integer index as arguments and removes the element at the index position from the list. If the index is invalid (i.e., it falls outside the bounds of the list), then this operation should raise an IndexError exception.

This function must return a 2-tuple of, in this order, the element previously at the specified index (i.e., the removed element) and the resulting list.

2 Linked List
In a file named linked_list.py, provide a data definition for an AnyList, whose Pair class’s first field can be any value. Amend our earlier definition to use None to represent the empty list. Be sure to call your pair class Pair, so that our tests can create objects correctly.

Implement the functions listed above.

Place your test cases in a file named linked_list_tests.py.

As before, follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design the each of these functions.

As always, write test cases as step three, before the template step.

3 Array List
In a file named array_list.py, define the List class(es) for an array list implementation and implement the aforementioned list operations. For this implementation, each element of the array represents one element of the list. This implementation must allow for the list to grow dynamically (i.e., you cannot assume a maximum size). Place your test cases in a file named array_list_tests.py.

As before, follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design the each of these functions.

You will use a Python list as the backing array for your array list implementation (Python lists, at least in the standard implementation, are backed by arrays).

Note: since this lab (and related project) is a study of data structure implementation, you are prohibited from using any of the operations of Python’s list type in your array list implementation aside from initializing with a specified size (through the * operator, e.g., [None] * 100, which will act as "allocating a new array") and indexing. This means that any copying required in your implementation must be done via loops to make the steps explicit (e.g., no slices allowed). This restriction only applies within this course when stated; when you use Python in the future and want an array-list like data structure, you should certainly use the provided type and its operations.

4 Exceptions and Testing
This lab requires you to signal an IndexError exception in several places. This means that you need to be able to raise exceptions, and to write tests for methods that raise them.

4.1 Raising Exceptions
In Python, you can raise an IndexError exception with the statement

raise IndexError()

This will cause Python to discard evaluation context outward until it reaches a try statement. Since we’re not using try statements yet, this means that it will discard all of the program’s evaluation context, and simply halt.

4.2 Testing Functions that Raise Exceptions
So, if raising an exception halts the program, how are we supposed to write tests for functions that raise exceptions?

Python provides an assertRaises method as part of its unittest framework that addresses this. However, there is one "gotcha." Let’s say your my_fun function is supposed to signal an IndexError when called with two equal numbers. We can test this using this expression:

self.assertRaises(IndexError, my_fun, 3, 3)

There’s something strange about this: we didn’t actually call the my_fun function, we just passed it to assertRaises.

You might be able to see why this is the case: in Python, as you know, arguments to function calls are evaluated before the call is made. This means that if we tried to use
my_fun(3,3)

as an argument to assertRaises, we would trigger the exception—and halt the program—before the assertRaises function can set up a fence to handle this exception.
5 Tuples
For the remove method, you’re asked to return a tuple. What’s a tuple?

Tuples are a way of representing a sequence of values of a known length. They’re easy to write. If you want to put the number 3 and the string "apple" in a 2-tuple, you’d write

(3, "apple")

This form can also be used to create tuples containing 3 elements, or zero elements. Unfortunately, you can’t use this form to create tuples with one element. Too bad.

How is a tuple different from an Array? In a typed language, they’d be completely different animals—for instance, you can associate different types with different elements of a tuple—but in Python, the differences are limited. For instance, you can’t call append on a tuple.

Let’s just say that if you want to write a function that returns two values, the idiomatic way to express that would be with a 2-tuple.

6 Lab Credit
You must submit your files for grading to receive credit for this lab. This requires that you use the specified file names (listed below) and the specified function names for the required operations (review the lab description to verify that these match).

Recall that the file names are as follows.
linked_list.py – linked list implementation

linked_list_tests.py – linked list tests

array_list.py – array list implementation

array_list_tests.py – array list tests