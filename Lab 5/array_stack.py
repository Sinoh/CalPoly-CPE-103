from array_list import *

# A Stack is
# A array list
# Takes in an array list and contains it
class Stack():
    def __init__(self, list = None):
        self.list = list

    def __repr__(self):
        return ('%s' % (self.list))

    def __eq__(self, other):
        if isinstance(other, Stack):
            return self.list == other.list
        else:
            return False

# None -> Stack
# Takes in nothing and returns and empty stack
def empty_stack():
        return Stack()

# Stack value -> Stack
# Given a stack and a value, returns a new stack with the value on top
def push(stack, value):
    if stack.list == None:
        return Stack((List(1, [value])))
    else:
        return Stack(add(stack.list,0,value))


# Stack -> stack
# Given a stack, returns a tuple with the removed value and the new list
def pop(stack):
    result = remove(stack.list,0)
    return (result[0], Stack(result[1]))


# Stack -> value
# Given a stack, returns the first element
def peek(stack):
    if stack.list == None:
        raise IndexError
    else:
        return stack.list.elements[0]

# Stack -> number
# Given a stack, returns the length of the stack
def size(stack):
    list = stack.list
    return length(list)

# Stack -> boolean
# Given a stack, returns true if its empty, and false if otherwise
def is_empty(stack):
    return stack.list == empty_list()


