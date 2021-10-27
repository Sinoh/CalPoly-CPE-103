# A Hashtable is
# None; or
# List[...] size
class Hashtable():
    def __init__(self, hash = None, size = 0, capacity = 0, collisions = 0):
        self.hash = [[] for i in range(capacity)] if hash is None else hash
        self.size = size
        self.capacity = capacity
        self.collisions = collisions

    def __repr__(self):
        return "%s, %i, %i, %i" % (self.hash, self.size, self.capacity, self.collisions)

    def __eq__(self, other):
        if isinstance(other, Hashtable):
            return self.hash == other.hash and self.size == other.size and self.capacity == other.capacity and self.collisions == other.collisions
        else:
            return False


# A empty_hash_table is
# A empty hash table with a size of 8
# None -> Hashtable
# Takes no parameters and returns an empty hash table with a size of 8
def empty_hash_table():
    return Hashtable(None, 0, 8)

# A get is
# A object
# Hashtable, key -> item
# Takes in a hashtable and key and returns the item with the corresponding key
def get(hashtable, key):
    if hashtable == None:
        raise LookupError()
    hashed = hash(key) % hashtable.capacity
    if hashtable.hash[hashed] != []:
        for tuples in hashtable.hash[hashed]:
            if key == tuples[0]:
                return tuples[1]
    raise LookupError()

# A remove is
# A Hashtable
# Hashtable key -> Hashtable
# Takes a Hashtable and key and returns the Hashtable with the key and corresponding item removed
def remove(hashtable, key):
    if hashtable == None:
        raise LookupError()
    hashed = hash(key) % hashtable.capacity
    if hashtable.hash[hashed] != []:
        for tuples in hashtable.hash[hashed]:
            if key == tuples[0]:
                hashtable.hash[hashed].remove(tuples)
                hashtable.size -= 1
                return hashtable
    raise LookupError()

# A size is
# A number
# Hashtable -> number
# Takes in a Hashtable and return the number of items in the Hashtable
def size(hashtable):
    if hashtable == None:
        return None
    return hashtable.size

# A load_factor is
# A number
# Hastable -> number
# Takes in a Hashtable and returns the current load factor of the Hashtable
def load_factor(hashtable):
    if hashtable == None:
        return 0
    return float(size(hashtable))/float(hashtable.capacity)


# An insert is
# A Hashtable
# Hashtable, number, item -> Hashtable
# Takes in a Hashtable, key, and an item and returns a new hash table with the item inserted in the correct place
# The item will be inserted based on the python-based hash
# If there is already a duplicated key in the table, the old key will be replaced
def insert(hashtable, key, item):
    if hashtable == None:
         return None
    hashed = hash(key) % (hashtable.capacity)

    # Checks if there is collision
    if hashtable.hash[hashed] != []:
        for i in range(len(hashtable.hash[hashed])):
            if key == hashtable.hash[hashed][i][0]:
                hashtable.collisions += 1
                remove(hashtable, key)
    hashtable.size += 1
    hashtable.hash[hashed].append((key, item))

    # Rehashes the whole list if the list's load factor is greater than 1.5
    if float(load_factor(hashtable)) >= 1.5:
        newtable = Hashtable(None, hashtable.size, hashtable.capacity * 2, hashtable.collisions)

        for hashes in hashtable.hash:
            if hashes != []:
                for tuples in hashes:
                    hashed = hash(tuples[0]) % newtable.capacity
                    newtable.hash[hashed].append(tuples)
        return newtable
    return hashtable

# A collision is
# a number
# Hashtable -> number
# Takes in a Hashtable and returns the number of collisions that occurred during the insert function
def collisions(hashtable):
    if hashtable == None:
        return None
    count = 0
    for hashes in (hashtable.hash):
        if hashes != []:
            count += len(hashes) - 1
    return count + hashtable.collisions