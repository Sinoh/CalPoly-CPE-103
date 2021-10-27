import unittest
from array_list import *

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

    def test_List(self):
        self.assertEqual(repr(List(2, ['a', 'b'])), "['a', 'b'] | Length: 2 | Capacity: 2")
        self.assertTrue(List(2, ['a', 'b']) == List(2, ['a', 'b']))
        self.assertFalse(List(2, ['a', 'b']) == List(1, ['a']))

    def test_empty_list(self):
        self.assertEqual(empty_list(), List())

    def test_add(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        result0 = List(1, ['a'])
        result1 = List(4, ['a', 'b', 'c', 'd'])
        result2 = List(4, ['d', 'a', 'b', 'c'])
        result3 = List(4, ['a', 'b', 'd', 'c'])
        self.assertEqual(add(list0, 0, 'a'), result0)
        self.assertEqual(add(list1, 3, 'd'), result1)
        self.assertEqual(add(list1, 0, 'd'), result2)
        self.assertEqual(add(list1, 2, 'd'), result3)
        self.assertRaises(IndexError, lambda: add(list0, -1, 'a'))
        self.assertRaises(IndexError, lambda: add(list1, 4, 'a'))

    def test_length(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        self.assertEqual(length(list0), 0)
        self.assertEqual(length(list1), 3)

    def test_get(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        self.assertRaises(IndexError, lambda: get(list0, 0))
        self.assertRaises(IndexError, lambda: get(list1, -1))
        self.assertRaises(IndexError, lambda: get(list1, 4))
        self.assertEqual(get(list1, 0), 'a')
        self.assertEqual(get(list1, 1), 'b')
        self.assertEqual(get(list1, 2), 'c')

    def test_set(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        result1 = List(3, ['d', 'b', 'c'])
        result2 = List(3, ['a', 'd', 'c'])
        result3 = List(3, ['a', 'b', 'd'])
        self.assertRaises(IndexError, lambda: set(list0, 0, 'a'))
        self.assertRaises(IndexError, lambda: set(list1, -1, 'a'))
        self.assertRaises(IndexError, lambda: set(list1, 3, 'a'))
        self.assertEqual(set(list1, 0, 'd'), result1)
        self.assertEqual(set(list1, 1, 'd'), result2)
        self.assertEqual(set(list1, 2, 'd'), result3)

    def test_remove(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        list2 = List(1, ['a'])
        result1 = ('a', List(2, ['b', 'c']))
        result2 = ('b', List(2, ['a', 'c']))
        result3 = ('c', List(2, ['a', 'b']))
        self.assertRaises(IndexError, lambda: remove(list0, 0))
        self.assertRaises(IndexError, lambda: remove(list1, -1))
        self.assertRaises(IndexError, lambda: remove(list1, 3))
        self.assertRaises(IndexError, lambda: remove(list2, 1))
        self.assertEqual(remove(list1, 0), result1)
        self.assertEqual(remove(list1, 1), result2)
        self.assertEqual(remove(list1, 2), result3)
        self.assertEqual(remove(list2, 0), list0)

if __name__ == '__main__':
    unittest.main()
