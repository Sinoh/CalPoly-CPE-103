# * Section 1 (Lists)
#change
import unittest

# * dd: NumList Data Definition

# A NumList is either
# Empty; or
# A Pair


# A linked list is either
# Empty; or
# A pair containing some value and the rest of the list

class Pair:
	def __init__(self, value, rest):
		self.value = value
		self.rest = rest 

	def __eq__(self,other):
		if isinstance(other, Pair):
			return self.value == other.value and self.rest == other.rest
		else:
			return False

# * 1:

# A Length is
# A number
# List number -> Number
# Takes a List and a counter, and counts up for each value
# def Length(Linkedlist):
# self.assertEqual(Length(Pair(12,Pair(8,'mt'))), 2)
# self.assertEqual(Length(Pair(2,Pair(27,Pair(22,'mt'))), 3))

def length(LinkedList,count=0):
	if LinkedList == 'mt':
		return count
	else:
		count += 1
		return length(LinkedList.rest,count)

# * 2:

# A Sum is
# A number
# List -> Number
# Takes a list and returns the sum of all the values in that list
# def sum(List):
# self.assertEqual(sum(Pair(12,Pair(8,'mt'))), 20)
# self.assertEqual(sum(Pair(2,Pair(27,Pair(22,'mt'))), 51))

def sum(List):
	if List == 'mt':
		return 0
	else:
		return  List.value + sum(List.rest)

# * 3:

# A count_greater_than is
# A list
# List number -> List
# Takes a list and returns all vaues greater than the given threshold number
# def count_greater_than(List, thresh):
# self.assertEqual(count_greater_than(Pair(12,Pair(8,'mt')),10), 1)
# self.assertEqual(count_greater_than(Pair(2,Pair(27,Pair(22,'mt')),10), 2)

def count_greater_than(List,thresh, count = 0):
	if List == 'mt':
		return count
	else:
		if List.value > thresh:
			count += 1
		return count_greater_than(List.rest,thresh,count)


# * 4:

# A find is
# A value
# List value -> number
# Takes a list and a value and returns the postion of the value in the list
# def find(List,value):
# self.assertEqual(find(Pair(12,Pair(8,'mt')),8), 1)
# self.assertEqual(find(Pair(2,Pair(27,Pair(22,'mt'))),22), 2)

def find(List,value,counter=0):
	if List == 'mt':
		return None
	else:
		if List.value == value:
			return counter
		else:
			return find(List.rest,value,counter+1)

# * 5:

# A sub_one_map is
# A linkedlist
# List -> List
# Takes a linkedlist and returns a new linkedlist with all values lowered by one
# def sub_one_map(List):
# self.assertEqual(sub_one_map(Pair(12,Pair(8,'mt')))), (Pair(11,Pair(7,'mt')))
# self.assertEqual(sub_one_map(Pair(2,Pair(27,Pair(22,'mt')))), Pair(1,Pair(28,Pair(21,'mt'))))

def sub_one_map(List):
	if List == 'mt':
		return 'mt'
	else:
		return Pair(List.value-1,sub_one_map(List.rest))

# * 6:

# A insert is
# A NumList
# List number -> List
# Takes a numlist in ascending order and a number and returns a new numlist with the number inserted in the proper location
# def insert(numlist,number):
# self.assertEqual(insert(Pair(12,Pair(8,'mt'))),10), (Pair(8,Pair(10,Pair(12,'mt'))))
# self.assertEqual(insert(Pair(27,Pair(22,Pair(2,'mt'))),10), Pair(2,Pair(10,Pair(2,Pair(27,'mt'))))

def insert(numlist,number):
	if numlist == 'mt':
		return Pair(number,'mt')
	else:
		if numlist.value > number:
			return Pair(number,numlist)
		else:
			return Pair(numlist.value,insert(numlist.rest,number))

# * Tests : the test case class for the list functions
x = Pair(12,Pair(8,'mt'))
y = Pair(2,Pair(27,Pair(22,'mt')))

class TestCase(unittest.TestCase):

	def test_length_1(self):
		self.assertEqual(length(x), 2)
	def test_length_2(self):
		self.assertEqual(length(y), 3)

	def test_sum_1(self):
		self.assertEqual(sum(x), 20)
	def test_sum_2(self):
		self.assertEqual(sum(y), 51)

	def test_count_greater_than_1(self):
		self.assertEqual(count_greater_than(x,10), 1)
	def test_count_greater_than_2(self):
		self.assertEqual(count_greater_than(y,10), 2)

	def test_find_1(self):
		self.assertEqual(find(x,8), 1)
	def test_find_2(self):
		self.assertEqual(find(y,22), 2)
	def test_find_3(self):
		z = 'mt'
		self.assertEqual(find(z,10), None)

	def test_sub_one_map_1(self):
		self.assertEqual(sub_one_map(x), Pair(11,Pair(7,'mt')))
	def test_sub_one_map_2(self):
		self.assertEqual(sub_one_map(y), Pair(1,Pair(26,Pair(21,'mt'))))

	def test_insert_1(self):
		x = Pair(8,Pair(12,'mt'))
		self.assertEqual(insert(x,10), Pair(8,Pair(10,Pair(12,'mt'))))
	def test_insert_2(self):
		y = Pair(2,Pair(22,Pair(27,'mt')))
		self.assertEqual(insert(y,10), Pair(2,Pair(10,Pair(22,Pair(27,'mt')))))
	def test_insert_3(self):
		z = 'mt'
		self.assertEqual(insert(z,1), Pair(1,'mt'))


if __name__ == '__main__':
	unittest.main()


