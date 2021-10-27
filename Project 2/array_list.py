import sys
sys.setrecursionlimit(10100)



# Helper Fn's
def elements_length(elements):
    if elements[0] is None:
        return 0
    else:
        count = 0
        for value in elements:
            if value != None:
                count += 1
        return count


def max_length(elements):
    count = 0
    for value in elements:
        count += 1
    return count



# An Array is
# - None; or
# - List([...]), length)


class List:
    def __init__(self, capacity=100, elements=None):
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


# An empty_list is
# - None
# None -> None
# Takes no arguments and return an empty list
def empty_list(length=100):
    return List(length)


# An add is
# - Array
# - Array index value -> Array
# Takes a list, index, and value of any type and places that value in the index of the list
def add(array, index, value, count = 0):
    if index < 0 or (isinstance(array, List) and index > array.length):
        if array != None and array.elements[0] == None:
            return List(2, [None, value])
        else:
            raise IndexError
    if array == None and index == 0:
        return List(1, [value])
    else:
        added = False
        result = empty_list(array.length + 1)
        for i in range(0,max_length(result.elements)):
            if i == index:
                result.elements[i] = value
                added = True
            else:
                if added == False:
                    j = i
                else:
                    j = i - 1
                result.elements[i] = array.elements[j]
        result.length = elements_length(result.elements)
        return result

# A length is
# a number
# Array -> number
# Takes an array and returns the number of elements
def length(array):
    if array == None:
        return 0
    return elements_length(array.elements)


# A get is a
# value
# Array index -> array
# Takes a array and an index and return the value at that index
def get(array, index):
    if array == None or array.length < index or index < 0:
        raise IndexError
    else:
        count = 0
        for value in array.elements:
            if count == index:
                return value
            else:
                count += 1


# An set is
# Array
# Array index value -> array
# Takes a Array, index, and value of any type and replaces the value in the index of the list with a new value
def set(array, index, value):
    if array == None or array.length - 1 < index or index < 0:
        raise IndexError
    else:
        result = empty_list(array.length)
        for i in range(0, max_length(result.elements)):
            if i == index:
                result.elements[i] = value
            else:
                result.elements[i] = array.elements[i]
        result.length = elements_length(result.elements)
        return result


# A remove is
# None or Array
# Array index -> tuple
# Takes a list, index and removes the value in the index of the list
def remove(array, index):
    if array == None or array.length -1 < index or index < 0:
        raise IndexError
    if elements_length(array.elements) == 1 and index == 0:
        return array.elements[0], None

    else:
        removed = False
        result = empty_list(array.length - 1)
        for i in range(0, max_length(array.elements)):
            if i == index:
                removed = True
            else:
                if removed == False:
                    j = i
                else:
                    j = i - 1
                result.elements[j] = array.elements[i]
        result.length = elements_length(result.elements)
        return (get(array, index), result)

# Pair Function -> None
# Apply the function to each object in Pair
def foreach(list, func):
    for i in range(list.length):
        if list.elements[i] != None:
            list.elements[i] = func(list.elements[i])




# Pair Pair int -> Pair
# Takes the source list, a temporary new list, and a key order and returns a new pair list in alphabetical order
def sort(list, order, func):
    if list == None or list == empty_list():
        return None
    else:
        result = empty_list()
        for i in range(length(list)):
            smallest = func(list, order)
            removed = remove(list, smallest)
            result = add(result, i, removed[0])
            list = removed[1]
    return result

# Pair int -> int
# Takes a array list and a key order and returns the index of the smallest value in the list follow this order:
# Default order is album -> artist -> title -> number
# The order can change based one the entered key in "find_key" function
def find_least(list, order):
    if list == None or list == empty_list():
        return None
    min_index = 0
    min_object = list.elements[0]
    if (list.elements[0]).isdigit:
        for i in range(1,length(list)):
            if list.elements[i] < min_object:
                min_index = i
                min_object = list.elements[i]

    else:
        test = getattr(list.element[0], 'album')
        for i in range(1,length(list)):
            key = 0
            while getattr(list.elements[i], order[key]) == getattr(min_object, order[key]):
                key += 1

            if getattr(list.elements[i], order[key]) < getattr(min_object, order[key]):
                min_index = i
                min_object = list.elements[i]

    return min_index


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


