import unittest
from array_stack import *

class TestStack(unittest.TestCase):
    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)

    def test_empty_stack(self):
        test0 = Stack(List(3,[1,2,'A']))
        result1 = Stack()
        self.assertEqual(empty_stack(), result1)

    def test_push(self):
        test0 = Stack(List(3,[1,2,'A']))
        result1 = Stack(List(4,[0,1,2,'A']))
        self.assertEqual(push(test0, 0), result1)


    def test_pop(self):
        test0 = Stack(List(3,[1,2,'A']))
        result1 = (1, Stack(List(3,[2,'A', None])))
        self.assertEqual(pop(test0), result1)


    def test_peek(self):
        test0 = Stack(List(3,[1,2,'A']))
        test1 = Stack()
        result1 = 1
        self.assertEqual(peek(test0), result1)
        self.assertRaises(IndexError, lambda: peek(test1))


    def test_size(self):
        test0 = Stack(List(3,[1,2,'A']))
        test1 = Stack()
        self.assertEqual(size(test0), 3)
        self.assertEqual(size(test1), 0)


    def test_is_empty(self):
        test0 = Stack(List(3,[1,2,'A']))
        test1 = Stack()
        test2 = Stack(List())
        self.assertFalse(is_empty(test0))
        self.assertTrue(is_empty(test2))
        self.assertFalse(is_empty(test1))

    def test_Stack(self):
        test1 = Stack(List(3,[1,2,'A']))
        test2 = Stack(List(3,[1,2,'A']))
        self.assertEqual(repr(Stack(List(3,[1,2,'A']))), "[1, 2, 'A'] | Length: 3 | Capacity: 3")
        self.assertTrue(test1 == test2)
        self.assertFalse(test2 == None)


if __name__ == "__main__":
    unittest.main()
