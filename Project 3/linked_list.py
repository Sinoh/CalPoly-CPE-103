import sys


# An Iterator is
# A number
# Tracks the position of the iterator within a given linked list

class Iterator():
    def __init__(self, list, pos = 0):
        self.list = list
        self.pos = pos

    def __repr__(self):
       return ('%s, %s' % (self.list, self.pos))

    def __eq__(self, other):
        if isinstance(other, Iterator):
            return self.list == other.list and self.pos == other.pos
        else:
            return False



# An AnyList is
# None; or
# A pair containing some value and the rest of the list


class Pair:
    def __init__(self, value = None, rest = None):
        self.value = value
        self.rest = rest

    def __repr__(self):
        return "%s, %s" % (self.value, self.rest)

    def __eq__(self,other):
        if isinstance(other, Pair):
            return self.value == other.value and self.rest == other.rest
        else:
            return False


# An empty_list is
# None
# None -> None
# Takes no arguments and return an empty list
def empty_list():
    return None

# An add is
# AnyList
# AnyList index value -> AnyList
# Takes a list, index, and value of any type and places that value in the index of the list
def add(AnyList, index, value, count = 0):
    if index < 0 or (AnyList == None and count < index):
        raise IndexError

    if AnyList == None and (count == index or count == 0):
        return Pair(value)
    if count == index:
        return Pair(value, Pair(AnyList.value, add(AnyList.rest, index, value, count + 1)))
    elif AnyList == None:
        return None
    else:
        return Pair(AnyList.value, add(AnyList.rest, index, value, count + 1))


# length is a
# number
# AnyList -> number
# Takes a AnyList and returns the number of values in the AnyList
def length(AnyList):
    if AnyList == None:
        return 0
    else:
        return 1 + length(AnyList.rest)


# A get is a
# value
# AnyList index -> AnyList
# Takes a AnyList and an index and return the value at that index
def get(AnyList, index, count = 0):
    if index < 0 or (AnyList == None and count <= index):
        raise IndexError

    elif count == index:
        return AnyList.value
    else:
        return get(AnyList.rest, index, count + 1)


# An set is
# AnyList
# AnyList index value -> AnyList
# Takes a list, index, and value of any type and replaces the value in the index of the list with a new value
def set(AnyList, index, value, count = 0):
    if index < 0 or (AnyList == None and count <= index):
        raise IndexError

    if AnyList == None:
        return None
    elif count == index:
        return Pair(value, set(AnyList.rest, index, value, count + 1))
    else:
        return Pair(AnyList.value, set(AnyList.rest, index, value, count + 1))


# A remove is
# None or AnyList
# AnyList index -> AnyList
# Takes a list, index and removes the value in the index of the list
def remove(AnyList, index):
    if index < 0 or index > length(AnyList) or AnyList == None:
        raise IndexError

    def helpremove(AnyList2, index2, count = 0):
        if count == index2:
            return helpremove(AnyList2.rest, index2, count + 1)
        elif AnyList2 == None:
            return None
        else:
            return Pair(AnyList2.value, helpremove(AnyList2.rest, index2, count + 1))

    return (get(AnyList, index), helpremove(AnyList, index))


# Pair Function -> None
# Apply the function to each object in Pair
def foreach(list, func):
    if list == None:
        return None
    else:
        list.value = func(list.value)
        foreach(list.rest, func)


# Linked-list -> number
# Given a linked-list, returns a value
def yield_iterator(list):
    while list.value != None:
        yield(list.value)
        list = list.rest

# A comes_before is
# A boolean
# vale value -> boolean
# Given two values, returns true if the first value comes before the second, otherwise false
def comes_before(val1, val2):
    if val1 < val2:
        return True
    else:
        return False

# A insert_sorted is
# A linked list
# Value Linked list function -> Linked List
# Given a value and a list and a function, returns a new list with the value inserted in the correct place
def insert_sorted(value, list, func):

    if list != None:
        if func(value, list.value):
            return Pair(value, list)
        else:
            return Pair(list.value, insert_sorted(value,list.rest,func))
    else:
        return Pair(value)









