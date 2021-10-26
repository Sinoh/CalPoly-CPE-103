from bst import *
import unittest

class TestList(unittest.TestCase):

    def test_BinarySearchTree(self):
        test1 = BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6)))
        test2 = BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6)))
        self.assertEqual(repr(test1), repr(BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6)))))
        self.assertTrue(test1 == test2)
        self.assertFalse(test2 == None)

    def test_comes_before(self):
        a = 1
        b = 2
        self.assertEqual(comes_before(a,b), True)
        self.assertEqual(comes_before(b,a), False)
        self.assertEqual(comes_before(a,None), False)

    def test_is_empty(self):
        test1 = BinarySearchTree(Node(5,Node(3,Node(2,None, Node(1)),Node(4)),Node(6)))
        test2 = BinarySearchTree(Node(None))
        self.assertEqual(is_empty(test1.root), False)
        self.assertEqual(is_empty(test2.root), True)

    def test_insert(self):
        test1 = BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6)))
        test2 = BinarySearchTree(Node(None))
        test3 = BinarySearchTree(Node(6, Node(3, Node(2, None, Node(1)), Node(4)), Node(7)))
        result1 = BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6,None,Node(7))))
        result2 = BinarySearchTree(Node(7))
        result3 = BinarySearchTree(Node(6, Node(3, Node(2, Node(0), Node(1)), Node(4)), Node(7)))
        self.assertEqual(insert(test1, 7), result1)
        self.assertEqual(insert(test2, 7), result2)
        self.assertEqual(insert(test3, 0), result3)

    def test_lookup(self):
        test1 = BinarySearchTree(Node(5, Node(3, Node(2, None, Node(1)), Node(4)), Node(6)))
        test2 = BinarySearchTree(Node(None))
        self.assertTrue(lookup(test1, 6))
        self.assertFalse(lookup(test1, 10))
        self.assertFalse(lookup(test2, 10))

    def test_delete(self):
        test0 = BinarySearchTree(None)
        test1 = BinarySearchTree(Node(0, Node(-12, Node(-19), Node(-9)), Node(11, Node(4), Node(17))))
        test2 = BinarySearchTree(Node(0, Node(-12, Node(-19)), Node(11, Node(4), Node(17))))
        result0 = BinarySearchTree(Node(0, Node(-12, Node(-19), Node(-9)), Node(17, Node(4))))
        result1 = BinarySearchTree(Node(0, Node(-12, Node(-19)), Node(11, Node(4), Node(17))))
        result2 = BinarySearchTree(Node(0, Node(-12, Node(-19)), Node(11, Node(4), Node(17))))
        test3 = BinarySearchTree(Node(10, Node(4, Node(-8), Node(6)), Node(24, Node(18), Node(42, Node(38), Node(50)))))
        result3 = BinarySearchTree(Node(10, Node(4, Node(-8), Node(6)), Node(38, Node(18), Node(42, None, Node(50)))))
        self.assertEqual(delete(test0, 0), test0)
        self.assertEqual(delete(test1, 11), result0)
        self.assertEqual(delete(test1, -9), result1)
        self.assertEqual(delete(test2, -10), result2)
        self.assertEqual(delete(test3, 24), result3)



if __name__ == '__main__':
    unittest.main()