import unittest
from bst import *

class TestList(unittest.TestCase):

    def test_prefix_iterator(self):
        list = BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6)))
        test1 = prefix_iterator(list)
        self.assertEqual(next(test1), 5)
        self.assertEqual(next(test1), 3)
        self.assertEqual(next(test1), 2)
        self.assertEqual(next(test1), 1)
        self.assertEqual(next(test1), 4)
        self.assertEqual(next(test1), 6)

    def test_infix_iterator(self):
        list = BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6)))
        test1 = infix_iterator(list)
        self.assertEqual(next(test1), 2)
        self.assertEqual(next(test1), 1)
        self.assertEqual(next(test1), 3)
        self.assertEqual(next(test1), 4)
        self.assertEqual(next(test1), 5)
        self.assertEqual(next(test1), 6)

    def test_postfix_iterator(self):
        list = BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6)))
        test1 = postfix_iterator(list)
        self.assertEqual(next(test1), 1)
        self.assertEqual(next(test1), 2)
        self.assertEqual(next(test1), 4)
        self.assertEqual(next(test1), 3)
        self.assertEqual(next(test1), 6)
        self.assertEqual(next(test1), 5)




if __name__ == '__main__':
    unittest.main()