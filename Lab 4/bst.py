
# Value Value -> Value
# Compares two values and returns True if the first value is less than the second and false otherwise
def comes_before(first,second):
    if first < second:
        return True
    else:
        return False


class BinarySearchTree():
    def __init__(self, root, func = comes_before):
        self.root = root
        self.func = func

    def __repr__(self):
        return ('%s, %s' % (self.root, self.func))

    def __eq__(self, other):
        if isinstance(other, BinarySearchTree):
            return self.root == other.root and self.func == other.func
        else:
            return False

class Node():
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return ('%s, %s, %s' % (self.value, self.left, self.right))

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value and self.left == other.left and self.right == other.right
        else:
            return False


# bst -> boolean
# Takes a binary search tree and returns true if the tree is empty, and false otherwise
def is_empty(node):
    if node.value == None:
        return True
    else:
        return False


# bst value -> bst
# Takes a binary search tree and a value and returns a new binary search tree with the value in the correct position
def insert(bst, value):

    def _insert(node, value, compare = bst.func):
        if is_empty(node):
            return Node(value)
        elif compare(value, node.value):
            if (node.left):
                _insert(node.left, value)
            else:
                node.left = Node(value)
        else:
            if (node.right):
                _insert(node.right, value)
            else:
                node.right = Node(value)
        return node

    return BinarySearchTree(_insert(bst.root,value))

# bst value -> boolean
# Takes a binary search tree and value and returns true if that value is within the tree and false otherwise
def lookup(bst,value):

    def _lookup(node, value, compare = bst.func):
        if node == None:
            return False
        elif (not compare(value, node.value)) and not compare(node.value, value):
            return True
        else:
            return _lookup(node.left, value) or _lookup(node.right, value)

    return _lookup(bst.root, value)

# bst value -> bst
# Takes a binary search tree and a value and returns a proper tree with the first instance of the value deleted
def delete(bst, value):


    def _delete(node, value, compare = bst.func):
        if node == None:
            return node
        else:
            if compare(value, node.value):
                return Node(node.value, _delete(node.left, value), node.right)
            if compare(node.value, value):
                return Node(node.value, node.left, _delete(node.right, value))

            else:
                if node.left == node.right == None:
                    return None

                elif node.right != None and node.left != None:
                    return Node(check_min(node.right), node.left, _delete(node.right, check_min(node.right)))


    def check_min(node, min_value = None, compare = bst.func):
        if min_value == None:
            min_value = node.value
        if node == None:
            return min_value
        else:
            if compare(node.value, min_value):
                min_value = node.value
            return check_min(node.left, min_value)





    return BinarySearchTree(_delete(bst.root, value))



# BinarySearchTree -> iterator
# Given a binary search tree, returns and iterator of the elements in prefix order
def prefix_iterator(bst):

    def prefix(node):
        if node:
            yield (node.value)

            yield from prefix(node.left)

            yield from prefix(node.right)

    return prefix(bst.root)

# BinarySearchTree -> iterator
# Given a binary search tree, returns and iterator of the elements in infix order
def infix_iterator(bst):

    def infix(node):
        if node:
            yield from infix(node.left)

            yield (node.value)

            yield from infix(node.right)

    return infix(bst.root)


# BinarySearchTree -> iterator
# Given a binary search tree, returns and iterator of the elements in postfix order
def postfix_iterator(bst):

    def postfix(node):
        if node:
            yield from postfix(node.left)


            yield from postfix(node.right)

            yield (node.value)

    return postfix(bst.root)