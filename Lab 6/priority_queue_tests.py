import unittest
from priority_queue import *

class TestQueue(unittest.TestCase):

    def test_elements_length(self):
        test0 = List()
        test1 = List(4,[1,2,3, None])
        self.assertEqual(elements_length(test0.elements), 0)
        self.assertEqual(elements_length(test1.elements), 3)

    def test_comes_before(self):
        self.assertTrue(comes_before(1,2))
        self.assertFalse(comes_before(2, -10))
        self.assertTrue(comes_before(1, None))
        self.assertFalse(comes_before(None, 1))

    def test_empty_queue(self):
        func = comes_before
        self.assertEqual(empty_pqueue(func), Pqueue(None,func))

    def test_enqueue(self):
        test0 = Pqueue()
        test1 = Pqueue(List(1,[1]))
        test2 = Pqueue(List(2,[1,2]))
        test3 = Pqueue(List(3,[1,2,3]))
        test4 = Pqueue(List(3,[1,3,4]))
        test5 = Pqueue(List(4,[1,2,3,4]))
        test6 = Pqueue(List(9, [1, 2, 3, 5, 6, 7, 8, 9, 10]))
        test7 = Pqueue(List(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        test8 = Pqueue(List(11, [-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        test9 = Pqueue(List(12, [-1, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertEqual(enqueue(test0, 1), test1)
        self.assertEqual(enqueue(test1, 2), test2)
        self.assertEqual(enqueue(test2, 3), test3)
        self.assertEqual(enqueue(test4, 2), test5)
        self.assertEqual(enqueue(test6, 4), test7)
        self.assertEqual(enqueue(test7, -1), test8)
        self.assertEqual(enqueue(test8, 0.5), test9)


    def test_dequeue(self):
        test3 = Pqueue(List(3, [1, 2, 3]))
        test2 = Pqueue(List(2, [2, 3]))
        test1 = Pqueue(List(1, [3]))
        test0 = Pqueue()
        self.assertEqual(dequeue(test3), (1, test2))
        self.assertEqual(dequeue(test2), (2, test2))
        self.assertEqual(dequeue(test1), (3, test1))
        self.assertRaises(IndexError, lambda: dequeue(test0))

    def test_peek(self):
        test0 = Pqueue()
        test1 = Pqueue(List(1, [1]))
        self.assertEqual(peek(test1), 1)
        self.assertRaises(IndexError, lambda: peek(test0))

    def test_size(self):
        test0 = Pqueue()
        test1 = Pqueue(List(1, [1]))
        self.assertEqual(size(test0), 0)
        self.assertEqual(size(test1), 1)
        self.assertEqual(size(empty_pqueue(comes_before)), 0)

    def test_is_empty(self):
        test0 = Pqueue()
        test1 = Pqueue(List(1, [1]))
        self.assertTrue(is_empty(test0))
        self.assertFalse(is_empty(test1))

    def test_queue(self):
        test0 = Pqueue(List(3, [1, 2, 3]))
        test1 = Pqueue(List(3, [1, 2, 3]))
        self.assertEqual(repr(test0), '[1, 2, 3] | Length: 3 | Capacity: 3, %s' % (test0.priority))
        self.assertTrue(test0 == test1)
        self.assertFalse(test1 == None)

if __name__ == "__main__":
    unittest.main()
