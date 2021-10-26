import unittest
import linked_list as list

class TestList(unittest.TestCase):

    def test_yield_iterator(self):
        test1 = list.yield_iterator(list.Pair(1, list.Pair(2, list.Pair(3))))
        self.assertEqual(next(test1),1)
        self.assertEqual(next(test1),2)
        self.assertEqual(next(test1),3)


if __name__ == '__main__':
    unittest.main()