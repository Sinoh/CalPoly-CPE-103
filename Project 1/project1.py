import unittest

# A StrList is either;
# A StrList; or
# Empty

class Pair:
	def __init__(self, value, rest):
		self.value = value
		self.rest = rest

	def __eq__(self,other):
		if isinstance(other, Pair):
			return self.value == other.value and self.rest == other.rest
		else:
			return False

# A ClassShape is;
# A name; and
# A StrList of names
class ClassShape:
	def __init__(self, name, StrList):
		self.name = name
		self.StrList = StrList


# A join_lines is
# A string
# StrList -> string
# Takes a StrList and joins all the strings in that list into a new string
def join_lines(StrList):
    if StrList == 'mt':
        return ''
    else:
        return StrList.value + '\n' + join_lines(StrList.rest)


# A fields_to_assignments are
# Lines of strings
# StrList -> StrList
# Take a StrList of field names and maps then to the lines of a __init__ definition
def fields_to_assignments(StrList):
    if StrList == 'mt':
        return 'mt'
    else:
        return Pair('        self.%s = %s' % (StrList.value, StrList.value), fields_to_assignments(StrList.rest))



# A commasep is a
# String
# StrList -> string
# Takes a StrList of field names and returns a string where the elements are joined together with a ", " preceding each element
def commasep(StrList):
    if StrList == 'mt':
        return ''
    else:
        return ', ' + StrList.value + commasep(StrList.rest)


# A init_method is a
# StrList
# StrList -> StrList
# Takes a StrList of field names and return the whole __init__ with the given field names
def init_method(StrList):
    if StrList == 'mt':
        return Pair('    def __init__(self):', Pair('        pass','mt'))
    else:
        return Pair('    def __init__(self' + commasep(StrList) + '):', fields_to_assignments(StrList))


# A fields_to_eq is are
# Lines of strings
# stringList -> StrList
# Take a StrList of field names and maps them to a StrList of Lines
def fields_to_eq(StrList):  # StrList cannot be empty!
    if StrList == 'mt':
        return Pair('                )', 'mt')
    else:
        return Pair('                and self.' + StrList.value + ' == other.' + StrList.value, fields_to_eq(StrList.rest))


# A eq_method is a
# StrList
# ClassShape -> StrList
# Takes a ClassShape and returns the __eq__ with the given StrList
def eq_method(ClassShape):
    if ClassShape.StrList == 'mt':
        return Pair('    def __eq__(self, other):', Pair('        pass', 'mt'))
    else:
        return Pair('    def __eq__(self, other):', Pair('        return (type(other) == ' + ClassShape.name, fields_to_eq(ClassShape.StrList)))

# A fields_to_repr is
# A StrList
# StrList -> string
# Takes a StrList of field names and return a StrList of the Eq logic
def fields_to_repr(StrList):
    if StrList == 'mt':
        return ''
    else:
        return 'self.%s, ' % StrList.value + fields_to_repr(StrList.rest)


# length is a:
# number
# StrList -> number
# Takes a StrList and returns the number of values in the StrList
def length(Strlist):
    if Strlist == 'mt':
        return 0
    else:
        return 1 + length(Strlist.rest)


# A repr_method is a
# StrList
# ClassShape -> StrList
# Takes a ClassShape and returns a StrList based on the StrList of the ClassShape

def repr_method(ClassShape):
    if ClassShape.StrList == 'mt':
        return Pair('    def __repr__(self):', Pair('        return \"%s\"' % ClassShape.name,'mt'))
    else:
        number_of_variables = (length(ClassShape.StrList) * '{!r}, ')[:-2]
        fields = fields_to_repr(ClassShape.StrList)[:-2]
        return Pair('    def __repr__(self):', Pair('        return \"%s(%s)\".format(%s)' % (ClassShape.name, number_of_variables,fields ),'mt'))


# A render_class is a
# Class
# ClassShape -> string
# Takes in a ClassShape and return the strings for a whole class definition

def render_class(ClassShape):
    init = join_lines(init_method(ClassShape.StrList))
    eq = join_lines(eq_method(ClassShape))
    repr = join_lines(repr_method(ClassShape))
    return 'class %s:\n%s\n%s\n%s' % (ClassShape.name, init, eq, repr)


class TestCase(unittest.TestCase):
    def test_join_lines(self):
        test1 =  'mt'
        test2 = Pair('Hello', Pair('World', 'mt'))
        result1 = ''
        result2 ='Hello\nWorld\n'
        self.assertEqual(join_lines(test1), result1)
        self.assertEqual(join_lines(test2), result2)

    def test_fields_to_assignemt(self):
        test1 = 'mt'
        test2 = Pair('Hello', Pair('World', 'mt'))
        result1 = 'mt'
        result2 = Pair('        self.Hello = Hello', Pair('        self.World = World', 'mt'))
        self.assertEqual(fields_to_assignments(test1), result1)
        self.assertEqual(fields_to_assignments(test2), result2)

    def test_commasep(self):
        test1 = 'mt'
        test2 = Pair('Hello', Pair('World', 'mt'))
        result1 = ''
        result2 = (', Hello, World')
        self.assertEqual(commasep(test1), result1)
        self.assertEqual(commasep(test2), result2)

    def test_init_method(self):
        test1 = 'mt'
        test2 = Pair('Hello', Pair('World', 'mt'))
        result1 = Pair('    def __init__(self):', Pair('        pass','mt'))
        result2 = Pair('    def __init__(self, Hello, World):', Pair('        self.Hello = Hello', Pair('        self.World = World', 'mt')))
        self.assertEqual(init_method(test1), result1)
        self.assertEqual(init_method(test2), result2)

    def test_fields_to_eq(self):
        test1 = 'mt'
        test2 = Pair('Hello', Pair('World', 'mt'))
        result1 = Pair('                )', 'mt')
        result2 = Pair('                and self.Hello == other.Hello', Pair('                and self.World == other.World', Pair('                )', 'mt')))
        self.assertEqual(fields_to_eq(test1), result1)
        self.assertEqual(fields_to_eq(test2), result2)


    def test_eq_method(self):
        str1 = 'mt'
        str2 = Pair('Hello', Pair('World', 'mt'))
        class1 = ClassShape('Test', 'mt')
        class2 = ClassShape('Test', str2)
        result1 = Pair('    def __eq__(self, other):', Pair('        pass', 'mt'))
        result2 = Pair('    def __eq__(self, other):', Pair('        return (type(other) == Test', Pair('                and self.Hello == other.Hello', Pair('                and self.World == other.World', Pair('                )', 'mt')))))
        self.assertEqual(eq_method(class1), result1)
        self.assertEqual(eq_method(class2), result2)

    def test_fields_to_repr(self):
        test1 = 'mt'
        test2 = Pair('Hello', Pair('World', 'mt'))
        result1 = ''
        result2 = 'self.Hello, self.World, '
        self.assertEqual(fields_to_repr(test1), result1)
        self.assertEqual(fields_to_repr(test2), result2)

    def test_length(self):
        test1 = 'mt'
        test2 = Pair('Hello', Pair('World', 'mt'))
        result1 = 0
        result2 = 2
        self.assertEqual(length(test1), 0)
        self.assertEqual(length(test2), 2)

    def test_repr_method(self):
        str1 = 'mt'
        str2 = Pair('Hello', Pair('World', 'mt'))
        class1 = ClassShape('Test', str1)
        class2 = ClassShape('Test', str2)
        result1 = Pair('    def __repr__(self):', Pair('        return "Test"','mt'))
        result2 = Pair('    def __repr__(self):', Pair('        return "Test({!r}, {!r})".format(self.Hello, self.World)', 'mt'))
        self.assertEqual(repr_method(class1), result1)
        self.assertEqual(repr_method(class2), result2)

    def test_render_class(self):
        str1 = 'mt'
        str2 = Pair('Hello', Pair('World', 'mt'))
        class1 = ClassShape('Test', str1)
        class2 = ClassShape('Test', str2)
        result1 = 'class Test:\n    def __init__(self):\n        pass\n\n    def __eq__(self, other):\n        pass\n\n    def __repr__(self):\n        return "Test"\n'
        result2 = 'class Test:\n    def __init__(self, Hello, World):\n        self.Hello = Hello\n        self.World = World\n\n    def __eq__(self, other):\n        return (type(other) == Test\n                and self.Hello == other.Hello\n                and self.World == other.World\n                )\n\n    def __repr__(self):\n        return "Test({!r}, {!r})".format(self.Hello, self.World)\n'
        self.assertEqual(render_class(class1), result1)
        self.assertEqual(render_class(class2), result2)
if __name__ == '__main__':
    unittest.main()
