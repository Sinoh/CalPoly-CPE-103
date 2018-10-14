# An AnyList is
# None; or
# A pair containing some value and the rest of the list


class Pair:
    def __init__(self, value, rest = None):
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
    if (0 <= index <= length(AnyList) + count) == False:
        raise IndexError

    if count == length(AnyList) + count:
        return Pair(value)
    elif count == index:
        return Pair(value, Pair(AnyList.value, AnyList.rest))
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
    if (0 <= index <= length(AnyList) + count) == False:
        raise IndexError
    if count == length(AnyList) + count:
        return None
    elif count == index:
        return AnyList.value
    else:
        return get(AnyList.rest, index, count + 1)

# An set is
# AnyList
# AnyList index value -> AnyList
# Takes a list, index, and value of any type and replaces the value in the index of the list with a new value
def set(AnyList, index, value, count = 0):
    if (0 <= index <= length(AnyList) + count) == False:
        raise IndexError

    if count == length(AnyList) + count:
        return Pair(value)
    elif count == index:
        return Pair(value, AnyList.rest)
    else:
        return Pair(AnyList.value, set(AnyList.rest, index, value, count + 1))

# A remove is
# None or AnyList
# AnyList index -> AnyList
# Takes a list, index and removes the value in the index of the list
def remove(AnyList, index):
    if (0 <= index <= length(AnyList)) == False:
        raise IndexError
    def helpremove(AnyList, index, count = 0):
        if count == index:
            count += 1
            return helpremove(AnyList.rest, index, count)
        elif AnyList is None:
            return None
        else:
            return Pair(AnyList.value, helpremove(AnyList.rest, index, count))
    return (get(AnyList, index), helpremove(AnyList, index))

