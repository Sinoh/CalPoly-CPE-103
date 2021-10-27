# lab-6-template

[Link](https://www.brinckerhoff.org/clements/2174-csc202/Labs/lab6.html)

For this lab you will explore one implementation of a priority queue (an alternate, typically more efficient, implementation is based on material not covered at this point). In addition, you will use your priority queue data structure to implement an event queue to enable the execution of events after specified durations of time.

1 Priority Queue
A priority queue behaves, in some respects, like a standard queue: elements are inserted at one end and extracted at the other. Unlike a standard queue, the order in which elements are extracted from a priority queue does not depend strictly on the order in which they were inserted. Instead, the elements are ordered by priority so that an element with higher priority will be extracted from the queue before elements of lower priority, even if the higher priority element was added last (one can think of a standard queue as being a priority queue where the priority is how recently the element was inserted; more recently would be lower priority).

1.1 To Do
For this implementation, when a priority queue is constructed the user must specify a function to use to determine the relative priority ordering between two elements (which can then be used to determine the order of all elements). More specifically, you can think of this function (of two arguments), comes_before , as being used to determine if the first argument should come before the second in the priority ordering (e.g., comes_before(1, 2) would return True if the elements should be in ascending order).

Write your priority queue implementation in a file named priority_queue.py with tests in priority_queue_tests.py.

Define each of the following functions. As always, follow the design recipe (data definitions if necessary, signature, purpose statement, header, test cases, fill in body) to design each of these functions.

empty_pqueue — this function takes an ordering function and returns an empty priority queue.

enqueue — given a priority queue and a value, enqueue adds the value to the queue. This operation is typically written to add the element not at the end of the queue (as would be the case for a standard queue), but in the appropriate position within the internal list as determined by the ordering function (i.e., store the elements in the proper order within the list to simplify the later operations). As such, searching for the position at which to insert should begin at the head of the backing list. This function returns the resulting priority queue.

dequeue — given a priority queue, removes the element at the beginning of the priority queue based on the ordering as determined by the ordering function. If there is no such element, raises an IndexError exception. This function must return a 2-tuple of, in this order, the element previously at the beginning of the priority queue and the resulting priority queue.

peek — given a priority queue, returns the element at the beginning of the queue based on the ordering as determined by the ordering function. If there is no such element, raises an IndexError exception.

size — given a priority queue, return the number of elements in the queue.

is_empty — given a priority queue, return True if the queue is empty, False otherwise.

2  Event Queue
In this part of the lab, you will put your priority queue implementation to use in the implementation of an event queue. This event queue will allow a user to schedule events to be executed (functions to be called) after a delay of a specified number of seconds (e.g., print something to the screen every three seconds, check for network activity every second, or download the new articles from a news feed every 10 minutes).

An event queue can be implemented by tracking a virtual "time" (an integer value representing the number of seconds that has passed; it should begin at 0) and by storing events with their scheduled times in a priority queue (where the scheduled time is the virtual "time" when the event is added plus the time delay for that event). In addition to scheduling events, the event queue will support running all events by waiting (delaying program execution) until events are ready.

2.1 To Do
In a file named event_queue.py, implement a new class, EventQueue, that uses a priority queue and that tracks the current virtual "time" (beginning at 0).

In the same file, define each of the following operations for the EventQueue.
add_event — given an EventQueue, a function to execute (the event), and a time delay (the number of seconds from now at which to execute), add_event stores the event to be scheduled in the EventQueue.

run_events — given an EventQueue, for as long as there are events, this function will wait (you can use time.sleep) until the "next" event in the queue is ready to execute. The function will then execute all "ready" events (i.e., all events scheduled to run at the current virtual "time"). This should continue until there are no events pending. (Note that you are not expected to account for the time required to run the events when updating the virtual time. In short, you may assume that each event takes 0 seconds to run.)

The code listing below demonstrates scheduling an event that will occur approximately every second. This event is repeated by scheduling it again every time it occurs. An additional event is included to stop the program after approximately 20 seconds. Add this code to a file named event_example.py.

Update the code two implement and schedule two additional events. One event should execute approximately every five seconds and the other should execute only a single time at approximately 15 seconds after the program begins.

 

from event_queue import *

import sys

 

def print_each_second(equeue):

   print('\ttime {}: every one'.format(equeue.time))

   add_event(equeue, print_each_second, 1)

 

 

def stop(equeue):

   print('\ttime {}: stopping'.format(equeue.time))

   sys.exit(0)

 

 

if __name__ == '__main__':

   equeue = EventQueue()

 

   add_event(equeue, stop, 20)

   add_event(equeue, print_each_second, 1)

 

   run_events(equeue)

 

3 Lab Credit
You must submit your files for grading to receive credit for this lab. This requires that you use the specified file names (listed below) and the specified function names for the required operations (review the lab description to verify that these match).

Recall that the file names are as follows.

priority_queue.py – priority queue implementation

priority_queue_tests.py – priority queue tests

event_queue.py – event queue implementation

event_example.py – example event program
