import unittest
from linked_list import *

class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_empty_list(self):
        result0 = None
        self.assertEqual(empty_list(), result0)


    def test_add(self):
        Anylist0 = None
        Anylist1 = Pair('a',Pair('b'))
        result1 = Pair('a', Pair('b', Pair('c')))
        result2 = Pair('a', Pair('c', Pair('b')))
        with self.assertRaises(IndexError):
            add(Anylist0, 5, 'c')
        self.assertEqual(add(Anylist1, 2, 'c'), result1)
        self.assertEqual(add(Anylist1,1, 'c'), result2)


    def test_length(self):
        Anylist0 = None
        Anylist1 = Pair('a', Pair('b'))
        result0 = 0
        result1 = 2
        self.assertEqual(length(Anylist0), result0)
        self.assertEqual(length(Anylist1), result1)

    def test_get(self):
        Anylist1 = Pair('a', Pair('b'))
        result1 = None
        with self.assertRaises(IndexError):
            get(Anylist1, 4)
        self.assertEqual(get(Anylist1, 2), result1)


    def test_set(self):
        Anylist1 = Pair('a', Pair('b',Pair('c')))
        result1 = Pair('a', Pair('c',Pair('c')))
        result2 = Pair('a', Pair('b', Pair('c', Pair('d'))))
        self.assertEqual(set(Anylist1,1, 'c'), result1)
        with self.assertRaises(IndexError):
            set(Anylist1,4,'x')
        self.assertEqual(set(Anylist1, 3, 'd'), result2)

    def test_remove(self):
        Anylist1 = Pair('a', Pair('b', Pair('c')))
        result1 = ('a', Pair('b', Pair('c')))
        self.assertEqual(remove(Anylist1, 0), result1)
        with self.assertRaises(IndexError):
            remove(Anylist1, 5)
        self.assertEqual(repr(Anylist1), 'a, b, c, None' )

if __name__ == '__main__':
    unittest.main()
