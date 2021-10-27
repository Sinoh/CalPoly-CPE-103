#* Section 1 (Git)

#*1) persnickety

#* Section 2 (Data Definitions)

#* 1) 

# Celsius is a float
# Return value as a float

#* 2)

# A price is an int

#* 3)

# Item is a price record

#* 4) 

# URL is a string
# date is represented as a number

#* Section 3 (Signature, Purpose Statements, Headers)

#* 1)

# List-of-float -> float
# Adds price and sales tax
# def total(price):

#* 2)

# String -> float
# Uses the name of an item to find the price
# def find_price(item):

#* 3)

# List-of-float -> Float
# Takes a list of income and returns the median income
# def median_income(list_of_income):

#* 4)

# String String -> Boolean
# Takes a geographic region and datatbase and returns true or false
# def overlap_region(database, region):

#* Section 4 (Test Cases)

#* 1)

# List-of-numbers -> number
# Takes three inputed numbers and returns the second highest value
def second_largest(num1,num2,num3):
	pass
# self.assertEqual(second_largest(1,2,3), 2)
# self.assertEqual(second_largest(6,4,5), 5)

#* 2)

# String -> Boolean
# Takes a string and returns a boolean depending if it has any capitals
def islower(string):
	pass
# self.assertEqual(islower(hello), True)
# self.assertEqual(islower(WORLD), False)

#* 3)
# String String -> String
# Takes two states that are strings and return the state that is upper north
def northern(state1, state2):
	pass
# self.assertEqual(nothern(California, Oregon), Oregon)
# self.assertEqual(nothern(California, Texas), California)

import unittest

class TestCase4(unittest.TestCase):
#1
	def test_second_largest_1(self):
		self.assertEqual(second_largest(1,2,3), 2)
	def test_secdon_largest_2(self):
		self.assertEqual(second_largest(6,4,5), 5)
#2
	def test_islower_1(self):
		self.assertEqual(islower(hello), True)
	def test_islower_2(self):
		self.assertEqual(islower(WORLD), False)
#3
	def test_northern_1(self):
		self.assertEqual(nothern(California, Oregon), Oregon)
	def test_northern_2(self):
		self.assertEqual(nothern(California, Texas), California)


#* Section 5 (Whole Functions)

#* 1)

# A length is a number that represent feet or meter
# Number -> Number
# Takes a number that represents feet and convert it into a number that represents meters
# def f2m(feet):

def f2m(feet):
	return float("%.2f" % (feet*0.3048))

#* 2)

# A Musical Note is pitch represented with a number in Hz and a duration represented with a number in seconds
# Number Number -> Number Number
# Takes in two numbers and returns a note
# class Note:
#	def _init__(self,Hz,duration):

class Note:
	def __init__(self,Hz,duration):
		self.Hz = Hz
		self.duration = duration

#* 3)

# A Musical Note is pitch represented with a number in Hz and a duration represented with a number in seconds
# Number -> Number
# Takes a Note and returns a new note with double the Hz
# def up_one_octave(Note):

def up_one_octave(note):
	return Note(note.Hz*2,note.duration)

#* 4)

# A Musical Note is pitch represented with a number in Hz and a duration represented with a number in seconds
# Number -> Number
# Takes a Note and doubles the Hz
# def up_one_octave_m(note):

def up_one_octave_m(note):
	note.Hz = note.Hz*2

note1 = Note(70,2)
note2 = Note(100,1)
newnote1 = up_one_octave(note1)
newnote2 = up_one_octave(note2)

class TestCase5(unittest.TestCase):
#1
	def test_f2m_1(self):
		self.assertEqual(f2m(3.28084), 1.00)
	def test_f2m_2(self):
		self.assertEqual(f2m(6), 1.83)
#2
	def test_Note_1(self):
		self.assertEqual((note1.Hz,note1.duration), (70,2))
	def test_Note_2(self):
		self.assertEqual((note2.Hz,note2.duration), (100,1))
#3
	def test_up_one_octave_1(self):
		self.assertEqual((newnote1.Hz,newnote1.duration), (140,2))
	def test_up_one_octave_2(self):
		self.assertEqual((newnote2.Hz,newnote2.duration), (200,1))
#4
	def test_up_one_octave_m_1(self):
		self.assertEqual(up_one_octave_m(note1), None)
		self.assertEqual((note1.Hz,note1.duration), (140,2))
	def test_up_one_octave_m_2(self):
		self.assertEqual(up_one_octave_m(note2), None)
		self.assertEqual((note2.Hz,note2.duration), (200,1))

if __name__ == '__main__':
    test_cases_to_run = [TestCase4, TestCase5]
    loader = unittest.TestLoader()

    suites_list = []
    for test_case in test_cases_to_run:
        suite = loader.loadTestsFromTestCase(test_case)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)
