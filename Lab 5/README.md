### CSC 202 Lab 5
Stacks, Queues, and Postfix Expressions

[Lab Specification](https://www.brinckerhoff.org/clements/2174-csc202/Labs/lab5.html)

#### Required Files
* `linked_list.py`
* `array_list.py`
* `linked_stack.py`
* `linked_stack_tests.py`
* `array_stack.py`
* `array_stack_tests.py`
* `postfix.py`
* `postfix_tests.py`
* `list_queue.py`
* `list_queue_tests.py`
* `circular_queue.py`
* `circular_queue_tests.py`


For this lab you will explore the implementation and use of two additional sequential data structures: the Stack and the Queue.

Invitation Link

1 Stack
You must provide two implementations of the Stack data structure. One implementation will be based on your Linked List implementation and the other will be based on your Array List implementation (from prior labs). Each Stack implementation must define each of the following functions.

As before, follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design each of these functions.

Write your linked list implementation in a file named linked_stack.py with tests in linked_stack_tests.py and your array list implementation in a file named array_stack.py with tests in array_stack_tests.py .

empty_stack — this function takes no arguments and returns an empty stack.

push — given a Stack and a value, adds the value to the top of the stack. This function returns the resulting stack.

pop — given a Stack, removes the top element. If there is no such element, raises an IndexError exception. This function must return a 2-tuple of, in this order, the element previously at the top of the stack (i.e., the popped element) and the resulting stack.

peek — given a Stack, returns the top element. If there is no such element, raises an IndexError exception. This function does not modify the stack.

size — given a Stack, returns the number of elements in the stack.

is_empty — given a Stack, returns True if the stack is empty, returns False otherwise.

2 Postfix Calculator
In this part of the lab you will use a Stack to implement a postfix expression calculator.

A postfix expression is one where the operands for a binary expression come before the operator. For instance, the expression

1 2 + 4 * evaluates by adding 1 and 2 (to get 3) and then multiplying the result by 4 (to get 12). Evaluation of such an expression can be implemented via a Stack. While processing the expression, each number is pushed onto the stack. When an operator (assuming for this exercise that each operator requires two operands, i.e., it is binary) is to be evaluated, the operands are popped from the stack, the calculation is performed, and the result is pushed back onto the stack. For example, the evaluation of 1 2 + 4 * would take place as follows.

 

Step                    Stack after Step

-------------           ------------------

                        top -> empty

1 => push 1             top -> 1

2 => push 2             top -> 2 1

+ =>

   pop                  top -> 1

   pop                  top -> empty

   push 1 + 2           top -> 3

4 => push 4             top -> 4 3

* =>

   pop                  top -> 3

   pop                  top -> empty

   push 3 + 4           top -> 12

 

2.1 To Do
In a file named postfix.py (with test cases in postfix_tests.py ) implement the following function.

Write a function, postfix_calc , that takes a string representing an expression in postfix form. Your function may assume that the string is properly formatted (i.e., if there is an error while processing the input, so be it). Split the string and process each element as demonstrated in the steps above to implement a postfix calculator. Your calculator must support the +, -, *, / operators (assume floating point values). Once the calculation is complete, return the value at the top of the stack.

As before, follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design this function.

3 Queue
You must provide two implementations of the Queue data structure. One of the implementations must be implemented as a circular buffer, as discussed below. The other should use a pair of linked lists, one representing the front of the queue, and the other the reversed tail of the queue, as discussed in class.

Your queue implementations should be able to handle 5,000 elements. This will require raising the recursion limit, unless you use a loop to implement your reverse function.

Each Queue implementation must define each of the following functions.

As before, follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design each of these functions.

Write your circular buffer implementation in a file named circular_queue.py with tests in circular_queue_tests.py . Write your other implementation in a file called list_queue.py , with tests in list_queue_tests.py .

empty_queue — this function takes no arguments and returns an empty queue.

enqueue — given a Queue and a value, enqueue adds the value to the end of the queue. This function returns the resulting queue.

dequeue — given a Queue, removes the element at the beginning of the queue. If there is no such element, raises an IndexError exception. This function must return a 2-tuple of, in this order, the element previously at the beginning of the queue (i.e., the dequeued element) and the resulting queue.

peek — given a Queue, returns the element at the beginning of the queue. If there is no such element, raises an IndexError exception. This function does not modify the queue.

size — given a Queue, return the number of elements in the queue.

is_empty — given a Queue, return True if the queue is empty, False otherwise.

3.1 Circular Buffer
Consider a queue implemented using an array list. If the enqueue operation were to add elements to the end of the list, then the dequeue operation would necessarily remove from the beginning of the list. This implies that, using a typical array list implementation, each dequeue would result in shifting (i.e., copying) all of the contents of the underlying array one position to toward the front. Since dequeueing is a common operation, such an implementation would incur a significant performance penalty.

Instead, for this lab, you will define a Queue implementation based on a circular buffer. This array will be of a fixed size (you should set the size to 5000 when the Queue is created). The fixed size simplifies the implementation of the circular buffer. Because the size of the array is fixed, you do not need to use your own array list implementation; you should simply use a Python list of a fixed size, and Python’s get and set operators.

The circular buffer allows for tracking the head of the queue as an index into the array. Values are not shifted as the result of a dequeue operation; instead, the index for the head of the queue is simply updated. Similarly, the number of elements currently in the queue is tracked and updated as values are enqueued. Left as such, this would waste the space at the beginning of the array after each dequeue operation. Instead, the queue itself will "wrap around" to the beginning of the array so that an attempt to enqueue an element that would normally put that element beyond the bounds of the array will instead put that element at the beginning of the array.

You are required to implement a Queue using a circular buffer. Since the buffer will be of fixed size (to simplify the implementation for the lab), any attempt to enqueue a value in a full Queue should fail with an exception (you should raise an IndexError as done in previous cases).

4 Lab Credit
You must submit your files for grading to receive credit for this lab. This requires that you use the specified file names (listed below) and the specified function names for the required operations (review the lab description to verify that these match).

Recall that the file names are as follows.

List implementations from prior lab:
linked_list.py – linked list implementation

array_list.py – array list implementation

Stack implementations:
linked_stack.py – linked list stack implementation

linked_stack_tests.py – linked list stack tests

array_stack.py – array list stack implementation

array_stack_tests.py – array list stack tests

Postfix calculator:
postfix.py – postfix calculator

postfix_tests.py – postfix calculator tests

Queue implementations:
list_queue.py – linked list queue implementation

list_queue_tests.py – linked list queue tests

circular_queue.py – circular queue implementation

circular_queue_tests.py – circular queue tests