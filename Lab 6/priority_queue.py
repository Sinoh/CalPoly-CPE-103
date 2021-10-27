import sys
sys.setrecursionlimit(5000)

# A comes_before is
# A boolean 
# Takes two numbers and return true if the first value is comes before the second
def comes_before(val1, val2):
    if val2 == None:
        return True
    if val1 == None:
        return False
    if val1 < val2:
        return True
    else:
        return False

# A elements_length
# Is a number
# List -> number
# Takes a list and  returns the number of values that are not 'Nones'
def elements_length(elements):
    if elements[0] == None:
        return 0
    else:
        count = 0
        for value in elements:
            if value == None:
                break
            count += 1
        return count

# An Array is
# - None; or
# - List([...]), length)
class List:
    def __init__(self, capacity=100, elements=None, length = 0):
        self.elements = [None] * capacity if elements is None else elements
        self.length = elements_length(self.elements)
        self.capacity = capacity

    def __repr__(self):
        return "%s | Length: %i | Capacity: %i" % (self.elements, self.length, self.capacity)

    def __eq__(self, other):
        if isinstance(other, List):
            return self.elements == other.elements and self.length == other.length and self.capacity == other.capacity
        else:
            return False

# A Queue is
# None or
# A list
# Takes in a list and contains is

class Pqueue():
    def __init__(self, list = None, priority = comes_before):
        self.list = list
        self.priority = priority

    def __repr__(self):
        return ('%s, %s' % (self.list, self.priority))

    def __eq__(self, other):
        if isinstance(other, Pqueue):
            return self.list == other.list and self.priority == other.priority
        else:
            return False


# A empty_Pqueue is
# A Queue with no list
# None -> Queue
# Takes in no arguements and returns an empty Queue
def empty_pqueue(func = None):
    return Pqueue(None,func)


# A enqueue is
# A Queue
# Queue value -> Queue
# Given a Queue and a value and returns a new Queue with the value added at the end
def enqueue(queue, value):

    if queue.list == None:
        return Pqueue(List(1,[value]))

    else:
        count = 0
        added = False
        result = Pqueue(List(queue.list.length + 1))
        for i in queue.list.elements:
            if added == True:
                result.list.elements[count] = i
                count += 1
                continue
            if queue.priority(value, i):
                result.list.elements[count] = value
                count += 1
                result.list.elements[count] = i
                count += 1
                added = True
            else:
                result.list.elements[count] = i
                count += 1
                if count == queue.list.length:
                    result.list.elements[count] = value
                    count += 1
        result.list.length = count
        return result






# A dequeue is
# A Queue
# Queue -> Queue
# Given a Queue, returns a tuple with the first value removed and the resulting Queue
def dequeue(queue):
    if (queue.list == None):
        raise IndexError()
    else:
        value = queue.list.elements[0]
        del queue.list.elements[0]
        queue.list.length -= 1
        queue.list.capacity -= 1
        return (value, queue)


# A peek is a
# value
# Queue -> value
# Given a queue, returns the first value in the queue
def peek(queue):
    if queue.list == None or queue.list.elements == None:
        raise IndexError
    else:
        return queue.list.elements[0]


# A size is
# A number
# Queue -> number
# Given a Queue, returns the number of elements in the Queue
def size(queue):
    if queue.list == None or queue.list.elements == None:
        return 0
    else:
        return queue.list.length


# A is_empty is
# A boolean
# Queue -> boolean
# Given a Queue, returns true if the Queue is empty, and false otherwise
def is_empty(queue):
    if queue.list == None or queue.list.elements == None:
        return True
    else:
        return False