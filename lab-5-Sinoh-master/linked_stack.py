from linked_list import *


# A Stack is
# A linked-list
# Takes in a linked list and contains it

class Stack():
    def __init__(self, list = None):
        self.list = list

    def __repr__(self):
        return ('%s' % (self.list))

    def __eq__(self,other):
        if isinstance(other, Stack):
            return self.list == other.list
        else: return False



# None -> Stack
# Takes in nothing and returns and empty stack
def empty_stack():
        return Stack()

# Stack value -> Stack
# Given a stack and a value, returns a new stack with the value on top
def push(stack, value):
    if stack.list == None:
        return Stack(Pair(value))
    else:
        list = stack.list
        return Stack(Pair(value,list))


# Stack -> stack
# Given a stack, returns a tuple with the removed value and the new list
def pop(stack):
    list = stack.list
    result = remove(list,0)
    return (result[0], Stack(result[1]))


# Stack -> value
# Given a stack, returns the first element
def peek(stack):
    if stack.list == None:
        raise IndexError()
    else:
        list = stack.list
        return list.value

# Stack -> number
# Given a stack, returns the length of the stack
def size(stack):
    list = stack.list
    return length(list)

# Stack -> boolean
# Given a stack, returns true if its empty, and false if otherwise
def is_empty(stack):
    return stack.list == empty_list()









