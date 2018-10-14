import sys


# A Queue is
# None or
# Two array lists
# Takes in a list and contains is
class Queue():
    def __init__(self, list = None,   en_index = 0, de_index = 0):
        self.list = [None] * 5000 if list == None else list
        self.en_index = en_index if en_index <= 5000 else 0
        self.de_index = de_index if de_index <= 5000 else 0

    def __repr__(self):
        return ("%s | En: %i | De: %i" % (self.list, self.en_index, self.de_index))

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.list == other.list and self.en_index == other.en_index and self.de_index == other.de_index
        else:
            return False


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
    if queue.list[queue.en_index] != None:
        raise IndexError
    else:
        queue.list[queue.en_index] = value
        queue.en_index += 1
        return queue


# A dequeue is
# A Queue
# Queue -> Queue
# Given a Queue, returns a tuple with the first value removed and the resulting Queue
def dequeue(queue):
    if queue.list[queue.de_index] == None:
        raise IndexError
    else:
        value = queue.list[queue.de_index]
        queue.list[queue.de_index] = None
        queue.de_index += 1
        return (value, queue)


# A peek is a
# value
# Queue -> value
# Given a queue, returns the first value in the queue
def peek(queue):
    if queue.list[queue.de_index] == None:
        raise IndexError
    return queue.list[queue.de_index]


# A size is
# A number
# Queue -> number
# Given a Queue, returns the number of elements in the Queue
def size(queue):
    count = 0
    for i in queue.list:
        if i != None:
            count += 1
    return count


# A is_empty is
# A boolean
# Queue -> boolean
# Given a Queue, returns true if the Queue is empty, and false otherwise
def is_empty(queue):
    for i in queue.list:
        if i != None:
            return False
    return True