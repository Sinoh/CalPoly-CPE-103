import unittest
from list_queue import *

class TestQueue(unittest.TestCase):
    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

    def test_reverse(self):
        test0 = Pair(1,Pair(2,Pair(3)))
        result1 = Pair(3, Pair(2, Pair(1)))
        self.assertEqual(reverse(test0), result1)

    def test_empty_queue(self):
        self.assertEqual(empty_queue(), Queue())

    def test_enqueue(self):
        test0 = Queue()
        test1 = Queue(Pair(1))
        test2 = Queue(Pair(2, Pair(1)))
        test3 = Queue(Pair('A', Pair(2, Pair(1))))
        self.assertEqual(enqueue(test0, 1), test1)
        self.assertEqual(enqueue(test1, 2), test2)
        self.assertEqual(enqueue(test2, 'A'), test3)


    def test_dequeue(self):
        test4 = Queue(None, Pair(1, Pair(2, Pair('A'))))
        test3 = Queue(Pair('A', Pair(2, Pair(1))))
        test2 = Queue(Pair(2, Pair(1)), None)
        test1 = Queue(Pair(1), None)
        test0 = Queue()
        self.assertEqual(dequeue(test4), ('A', test2))
        self.assertEqual(dequeue(test3), ('A', test2))
        self.assertEqual(dequeue(test2), (2, test1))
        self.assertEqual(dequeue(test1), (1, test0))
        self.assertRaises(IndexError, lambda: dequeue(test0))

    def test_peek(self):
        test0 = Queue(Pair(1, Pair(2, Pair('A'))))
        test1 = Queue()
        test2 = Queue(Pair(1, Pair(2, Pair('A'))), Pair('A', Pair(2, Pair(1))))
        self.assertEqual(peek(test0), 'A')
        self.assertEqual(peek(test2), 'A')
        self.assertRaises(IndexError, lambda: peek(test1))

    def test_size(self):
        test0 = Queue(Pair(1, Pair(2, Pair('A'))))
        test1 = Queue()
        self.assertEqual(size(test0), 3)
        self.assertEqual(size(test1), 0)

    def test_is_empty(self):
        test0 = Queue(Pair(1, Pair(2, Pair('A'))))
        test1 = Queue()
        self.assertFalse(is_empty(test0))
        self.assertTrue(is_empty(test1))

    def test_queue(self):
        test0 = Queue(Pair(1, Pair(2, Pair('A'))))
        test1 = Queue(Pair(1, Pair(2, Pair('A'))))
        self.assertEqual(repr(test0), '1, 2, A, None, None')
        self.assertTrue(test0 == test1)
        self.assertFalse(test1 == None)
if __name__ == "__main__":
    unittest.main()
