# Helper Fn's
def elements_length(elements):
    if elements[0] is None:
        return 0
    else:
        count = 0
        for value in elements:
            if value == None:
                break
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
    if (0 <= index <= (length(array) + count)) == False:
        raise IndexError
    if array == None and index == 0:
        return List(1, [value])
    else:
        result = empty_list(array.length +1)
        for i in range(0,max_length(result.elements)):
            if i == index:
                result.elements[i] = value
                j = i
                result.elements[i] = array.elements[j]
            else:
                j = i
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
    if (0 <= index <= (length(array))) == False:
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
    if (0 <= index <= (length(array))) == False:
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
    if (0 <= index <= (length(array))) == False:
        raise IndexError
    if elements_length(array.elements) == 1 and index == 0:
        return None
    else:
        result = empty_list(array.length - 1)
        for i in range(0, max_length(array.elements)):
            if i == index:
                j = i - 1
                result.elements[j] = array.elements[i]
            else:
                j = i
                result.elements[j] = array.elements[i]
        result.length = elements_length(result.elements)
        return (get(array, index), result)




