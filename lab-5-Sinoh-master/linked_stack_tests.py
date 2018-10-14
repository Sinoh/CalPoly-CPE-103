import unittest
from linked_stack import *

class TestStack(unittest.TestCase):
    def test00_interface(self):
        test_stack = empty_stack()
        test_stack = push(test_stack, "foo")
        peek(test_stack)
        _, test_stack = pop(test_stack)
        size(test_stack)
        is_empty(test_stack)

    def test_empty_stack(self):
        test0 = Stack(Pair(1,Pair(2,Pair('A'))))
        result1 = Stack()
        self.assertEqual(empty_stack(),result1)

    def test_push(self):
        test0 = Stack(Pair(1, Pair(2, Pair('A'))))
        test1 = Stack()
        result1 = Stack(Pair(0, Pair(1,Pair(2,Pair('A')))))
        result2 = Stack(Pair(0))
        self.assertEqual(push(test0, 0), result1)
        self.assertEqual(push(test1,0), result2)


    def test_pop(self):
        test0 = Stack(Pair(1, Pair(2, Pair('A'))))
        result1 = (1, Stack(Pair(2,Pair('A'))))
        self.assertEqual(pop(test0), result1)


    def test_peek(self):
        test0 = Stack(Pair(1, Pair(2, Pair('A'))))
        test1 = Stack()
        result1 = 1
        self.assertEqual(peek(test0),result1)
        self.assertRaises(IndexError, lambda: peek(test1))

    def test_size(self):
        test0 = Stack(Pair(1, Pair(2, Pair('A'))))
        self.assertEqual(size(test0), 3)


    def test_is_empty(self):
        test0 = Stack(Pair(1, Pair(2, Pair('A'))))
        test1 = Stack()
        test2 = Stack(Pair())
        self.assertFalse(is_empty(test0))
        self.assertTrue(is_empty(test1))
        self.assertFalse(is_empty(test2))

    def test_Stack(self):
        test1 = Stack(Pair(1, Pair(2, Pair('A'))))
        test2 = Stack(Pair(1, Pair(2, Pair('A'))))
        self.assertEqual(repr(Stack(Pair(1, Pair(2, Pair('A'))))), "1, 2, A, None")
        self.assertTrue(test1 == test2)
        self.assertFalse(test1 == None)


if __name__ == "__main__":
    unittest.main()
