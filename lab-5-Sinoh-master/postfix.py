import operator
from linked_stack import *

# A postfix_calc is
# A stack
# Stack string -> stack
# Takes a stack and a string and return the calculated value on top of the stack
def postfix_calc(string, stack = empty_stack()):
    list = string.split(' ')
    number = []
    operant = []
    ops = {'+': operator.add, '-': operator.sub, '*' : operator.mul, '/' : operator.truediv }
    for i in list:
        if i in ['+', '-', '*', '/']:
            operant.append(i)
        elif i.isdigit():
            number.append(i)


    stack = push(stack, float(number[0]))
    del number[0]
    while len(number) != 0:
        stack = push(stack, float(number[0]))
        del(number[0])

        value2 = pop(stack)
        value1 = pop(value2[1])
        newvalue = ops[operant[0]](float(value1[0]), float(value2[0]))
        del(operant[0])

        stack = push(empty_stack(), newvalue)


    return peek(stack)