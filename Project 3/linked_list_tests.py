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


    def test_linked_list(self):
        test0 = Iterator([1, 2, 3], 0)
        test1 = Iterator([1, 2, 3], 0)
        self.assertEqual(repr(test0), '[1, 2, 3], 0')
        self.assertTrue(test0 == test1)
        self.assertFalse(test0 == None)
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
        result1 = 'b'
        with self.assertRaises(IndexError):
            get(Anylist1, 4)
        self.assertEqual(get(Anylist1, 1), result1)


    def test_set(self):
        Anylist1 = Pair('a', Pair('b',Pair('c')))
        result1 = Pair('a', Pair('c',Pair('c')))
        self.assertEqual(set(Anylist1,1, 'c'), result1)
        self.assertRaises(IndexError, lambda: set(Anylist1,4,'x'))

    def test_remove(self):
        Anylist1 = Pair('a', Pair('b', Pair('c')))
        result1 = ('a', Pair('b', Pair('c')))
        self.assertEqual(remove(Anylist1, 0), result1)
        self.assertRaises(IndexError, lambda: remove(Anylist1, 5))
        self.assertEqual(repr(Anylist1), 'a, b, c, None' )

    def test_foreach(self):
        def func(x):
            if str(x).isalpha():
                return x
            else:
                return x*2
        list0 = None
        list1 = Pair(1, Pair('A', Pair(2)))
        result1 = Pair(2, Pair('A', Pair(4)))
        self.assertIsNone(foreach(list0, func))
        self.assertIsNone(foreach(list1, func))


    def test_yield_iterator(self):
        test1 = yield_iterator(Pair(1, Pair(2, Pair(3))))
        self.assertEqual(next(test1),1)
        self.assertEqual(next(test1),2)
        self.assertEqual(next(test1),3)

    def test_insert_sorted(self):
        test0 = Pair(1,Pair(2,Pair(5)))
        test1 = Pair(1,Pair(2,Pair(4, Pair(5))))
        test2 = Pair(1, Pair(2, Pair(4, Pair(5, Pair(6)))))
        self.assertEqual(insert_sorted(4, test0,comes_before), test1)
        self.assertEqual(insert_sorted(6, test1,comes_before), test2)



if __name__ == '__main__':
    unittest.main()
