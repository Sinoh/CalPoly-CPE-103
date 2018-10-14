from linked_list import *
import unittest

class TestList(unittest.TestCase):

    def test_iterator(self):
        test1 = Iterator(Pair(1,Pair(2,Pair(3))))
        test2 = Iterator(Pair(1,Pair(2,Pair(3))))
        self.assertEqual(repr(test1), repr(Iterator(Pair(1,Pair(2,Pair(3))), 0)))
        self.assertTrue(test1 == test2)
        self.assertFalse(test2 == None)

    def test_object_iterator(self):
        test1 = Pair(1, Pair(2, Pair(3)))
        result1 = Iterator(Pair(1,Pair(2,Pair(3))))
        self.assertEqual(object_iterator(test1), result1)

    def test_has_next(self):
        test1 = Iterator(Pair(1, Pair(2, Pair(3))))
        test2 = Iterator(Pair(1, Pair(2, Pair(3))),3)
        self.assertTrue(has_next(test1))
        self.assertFalse(has_next(test2))

    def test_next_it(self):
        test1 = Iterator(Pair(1, Pair(2, Pair(3))))
        test2 = Iterator(Pair(1, Pair(2, Pair(3))), 3)
        self.assertEqual(next(test1),1)
        self.assertRaises(StopIteration, lambda: next(test2))



if __name__ == '__main__':
    unittest.main()