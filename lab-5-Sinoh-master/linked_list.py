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
    if index < 0 or AnyList == None:
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

# Pair Pair int -> Pair
# Takes the source list, a temporary new list, and a key order and returns a new pair list in alphabetical order
def sort(list, func, order = ['album', 'artist', 'title', 'number'], newlist = empty_list()):
    if list == None:
        return newlist
    smallest = func(list, order)
    removed = remove(list, smallest)
    newerlist = add(newlist, length(newlist), removed[0])
    return sort(removed[1], func, order, newerlist)



# Pair int -> int
# Takes a pair list and a key order and returns the index of the smallest value in the list follow this order:
# Default order is album -> artist -> title -> number
# The order can change based one the entered key in "find_key" function
def find_least(list, order):
    if list == None:
        return None

    def _find_least(list, order, min_index = 0, min_object=list.value, count = 0):
        if list.rest == None:
            return min_index
        else:
            key = 0
            while getattr(min_object, order[key]) == getattr(list.rest.value, order[key]):
                key += 1
            count += 1
            if getattr(min_object, order[key]) > getattr(list.rest.value, order[key]):
                min_index = count
                min_object = list.rest.value
            return _find_least(list.rest, order, min_index, min_object, count)

    return _find_least(list, order)



# int -> list
# Takes an number from 0 to 3 and returns a list with that value first, then the rest of the numbers
def find_key(key):
    if key not in [0, 1, 2, 3]:
        print('... Invalid sort option')
        sys.exit()
    else:
        order = ['album', 'artist', 'title', 'number']
        order2 = ['number', 'title', 'artist', 'album']
        neworder = [order2[key]]
        for i in range(4):
            if order2[i] != order[key]:
                neworder.append(order[i])
    return neworder


# Linked-List -> Iterator
# Takes a linked-list and returns the object iterator
def object_iterator(list):
    return Iterator(list)

# Iterator -> boolean
# Takes an iterator object and returns true if there is another value to return from the iterator list
def has_next(object):
    if object.pos < length(object.list):
        return True
    else:
        return False

# Iterator -> value
# Takes an iterator object and returns the next value or a raised exception if it is the end of the list
def next(object):
    if not has_next(object):
        raise StopIteration
    else:
        value = object.list.value
        object.list = object.list.value
        object.pos += 1
        return value


# Linked-list -> number
# Given a linked-list, returns a value
def yield_iterator(list):
    while list.value != None:
        yield(list.value)
        list = list.rest











