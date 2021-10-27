from huffman_bits_io import *
import array_list as ar
import linked_list as li


# A file_array is
# Is a List
# file -> list
# Takes a given file and opens that text file and counts the frequency of occurrences of each character
# The given file should be only 8-Bit ASCII characters

def file_array(file):
    alist = ar.List(256, [0] * 256, 256)
    for obj in file:
        og = obj
        for char in obj:
            alist.elements[ord(str(char))] += 1
    return (alist,og)


# A Leaf is
# A integer of a chraracter and its number of occurance
class Leaf():
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency

    def __repr__(self):
        return ('%s, %s') % (self.character, self.frequency)

    def __eq__(self, other):
        if isinstance(other, Leaf):
            return self.character == other.character and self.frequency == other.frequency
        else:
            return False

# A Huffmantree is
# A node containing the integer of a character, that character's frequency, the left and right subtree
class Huffmantree():
    def __init__(self, character, frequency , left, right):
        self.character = character
        self.frequency = frequency
        self.left = left
        self.right = right

    def __repr__(self):
        return ('%s, %s, %s, %s') % (self.character, self.frequency, self.left, self.right)

    def __eq__(self, other):
        if isinstance(other, Huffmantree):
            return self.character == other.character and self.frequency == other.frequency and self.left == other.left and self.right == other.right
        else:
            return False


# A comes_before is
# A boolean
# Tree Tree -> Boolean
# Takes two trees and returns True if the first tree value comes before the second, otherwise False
def comes_before(treea, treeb):
    if treea.frequency != treeb.frequency:
        return treea.frequency < treeb.frequency
    else:
        if treea.character == None:
            return False
        if treeb.character == None:
            return True
        return treea.character < treeb.character

# Array_to_linked
# A Pair
# array_list -> Pair
# Takes a array_list and returns a sorted linked list
def array_to_linked(array_list):
    newlist = li.empty_list()
    for i in range(array_list.length):
        freq = array_list.elements[i]
        if freq != 0:
            newlist = li.insert_sorted(Leaf(i, freq), newlist, comes_before)
    return newlist



# A build_huff_tree is
# A binary tree
# List -> binarytree
# Takes a list of character and its frequency, and returns a proper huffman tree
def build_huff_tree(list):
    leaf1 = list.value
    leaf2 = list.rest.value
    return Huffmantree(None, leaf1.frequency + leaf2.frequency, leaf1, leaf2)


# A connect_nodes is
# A binary tree
# Linked_list -> Binary Tree
# Takes a a sorted linked list of the frequency of characters and returns a huffman binary tree
def connect_nodes(list):
    if list.rest != None:
        tree = build_huff_tree(list)
        return connect_nodes(li.insert_sorted(tree, list.rest.rest, comes_before))
    else:
        return list.value

# A tree_traversal is
# A str
# Binary_Tree -> String
# Takes a huffman tree and traverses it and returns each character from left to right
def tree_traversal(tree, string=''):
    if isinstance(tree, Leaf):
        return  string + chr(tree.character)
    else:
        return tree_traversal(tree.left, string) + tree_traversal(tree.right, string)

# An encoder is
# A str
# Binary tree -> string
# Given a huffman tree, will go down every path and keeps track of which path it takes to get to a specific leaf
def encoder(tree):
    arr_list = ar.empty_list(256)

    def _encoder(tree, code = ''):
        if isinstance(tree, Leaf):
            arr_list.elements[tree.character] = code
            arr_list.length += 1
        else:
            _encoder(tree.left, code + '0')
            _encoder(tree.right,code + '1')
        return arr_list

    return _encoder(tree)

# A encode is
# A string
# String list -> string
# Takes the encoded list and the original string and encodes the string
def encode(string, encoded):
    result = ''
    for char in string:
        result += encoded.elements[ord(char)]
    return result


# A huffman_encode is
# A str
# str str -> str
# Takes in an input text file and the name of an output text file, the encodes the inputted text onto the outputted file
def huffman_encode(input,output):
    file = open(input)
    huff_write = HuffmanBitsWriter(output)

    tuple = file_array(file)
    chr_arr = tuple[0]
    og = tuple[1]
    chr_linked = array_to_linked(chr_arr)
    tree = connect_nodes(chr_linked)
    encoded_list = encoder(tree)
    traversed = tree_traversal(tree)
    code = encode(og, encoded_list)


    huff_write.write_byte(len(traversed))
    for obj in range(chr_arr.length):
        if chr_arr.elements[obj]!= 0:
            huff_write.write_byte(obj)
            huff_write.write_int(chr_arr.elements[obj])
    huff_write.write_code(code)

    file.close()
    huff_write.close()
    return traversed



# A get_frequency is
# A str
# Str -> List
# Takes a string of bytes as a input, and returns a array list with the frequency of each character
def get_frequency(file):
    newlist = ar.List(256, [0] * 256, 256)
    num_of_codes = file.read_byte()
    for obj in num_of_codes:
        code = file.read_byte()
        occurences = file.read_int()
        newlist.elements[code] = occurences
    return newlist



# A decoder is
# A Str
# List -> list
# Takes a array list and returns a string of the characters
def decoder(list):
    strings = []
    for obj in list.elements:
        if obj != 0:
            strings.append(obj)
    return strings

# A huffman_decode is
# A Str
# Str Str -> Str
# Takes in an input text file and the name of an output text file, the decodes the inputted text onto the outputted file
def huffman_decode(input, output):
    file = HuffmanBitsReader(input)
    out = open(output, 'w')

    frequency = get_frequency(file)
    linked_list = array_to_linked(frequency)
    tree = connect_nodes(linked_list)
    decoded_list = decoder(frequency)
    

















