from linked_stack import *
sys.setrecursionlimit(5000)

# A Queue is
# None or
# Two linked list
# Takes in a list and contains is

class Queue():
    def __init__(self,  early= None, late = None):
        self.early = early
        self.late = late

    def __repr__(self):
        return ('%s, %s' % (self.early, self.late))

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.early== other.early and self.late == other.late
        else:
            return False


# A reverse is
# A Queue
# list -> list
# Takes a list and reverses the order of the list
def reverse(list, rest = None):
    if list == None:
        return rest
    rest =Pair(list.value, rest)
    return reverse(list.rest, rest)


# A empty_Queue is
# A Queue with no list
# None -> Queue
# Takes in no arguements and returns an empty Queue
def empty_queue():
    return Queue()


# A enqueue is
# A Queue
# Queue value -> Queue
# Given a Queue and a value and returns a new Queue with the value added at the end
def enqueue(queue, value):
    return Queue(Pair(value, queue.early))


# A dequeue is
# A Queue
# Queue -> Queue
# Given a Queue, returns a tuple with the first value removed and the resulting Queue
def dequeue(queue):
    if (queue.early == None):
        if (queue.late == None):
            raise IndexError()
        else:
            new_early = reverse(queue.late)
            return (new_early.value, Queue(new_early.rest, None))
    else:
        return (queue.early.value, Queue(queue.early.rest, queue.late))


# A peek is a
# value
# Queue -> value
# Given a queue, returns the first value in the queue
def peek(queue):
    if queue == empty_queue():
        raise IndexError
    else:
        if queue.late == None:
            queue.late = reverse(queue.early)
            return queue.late.value
        else:
            return queue.late.value


# A size is
# A number
# Queue -> number
# Given a Queue, returns the number of elements in the Queue
def size(queue):
    return length(queue.early) + length(queue.late)


# A is_empty is
# A boolean
# Queue -> boolean
# Given a Queue, returns true if the Queue is empty, and false otherwise
def is_empty(queue):
    if queue == empty_queue():
        return True
    else:
        return False