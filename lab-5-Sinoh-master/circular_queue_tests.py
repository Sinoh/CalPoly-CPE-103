import unittest
from circular_queue import *

class TestQueue(unittest.TestCase):
    def test00_interface(self):
        test_queue = empty_queue()
        test_queue = enqueue(test_queue, "foo")
        peek(test_queue)
        _, test_queue = dequeue(test_queue)
        size(test_queue)
        is_empty(test_queue)

    def test_Queue(self):
        test0 = Queue([1,2,'A'])
        test1 = Queue([1,2,'A'])
        self.assertEqual(repr(test0), "[1, 2, 'A'] | En: 0 | De: 0")
        self.assertTrue(test0 == test1)
        self.assertFalse(test1 == None)

    def test_empty_queue(self):
        self.assertEqual(empty_queue(), Queue())

    def test_enqueue(self):
        test0 = empty_queue()
        queue = empty_queue()
        queue.list[queue.en_index] = 1
        queue.en_index += 1
        self.assertEqual(enqueue(test0, 1), queue)
        test1 = Queue([])
        self.assertRaises(IndexError, lambda: enqueue(test1, 2))

    def test_dequeue(self):
        test0 = Queue([1,2,3,4])
        queue = Queue([None, 2,3,4])
        queue.de_index += 1
        self.assertEqual(dequeue(test0), (1, queue))
        self.assertRaises(IndexError, lambda: dequeue(Queue()))

    def test_peek(self):
        test0 = Queue([1, 2, 3, 4])
        test1 = Queue()
        self.assertEqual(peek(test0), 1)
        self.assertRaises(IndexError, lambda: peek(test1))


    def test_size(self):
        test0 = Queue([1, 2, 3, 4])
        test1 = Queue()
        self.assertEqual(size(test0), 4)
        self.assertEqual(size(test1), 0)

    def test_is_empty(self):
        test0 = Queue([1, 2, 3, 4])
        test1 = Queue()
        self.assertFalse(is_empty(test0))
        self.assertTrue(is_empty(test1))
if __name__ == "__main__":
    unittest.main()

