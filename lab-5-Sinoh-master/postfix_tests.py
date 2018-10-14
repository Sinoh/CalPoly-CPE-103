import unittest
from postfix import *

class TestList(unittest.TestCase):
    def test_postfix_calc(self):
        test1 = "5"
        result1 = 5.0
        test2 = "1 2 +"
        result2 = 3.0
        test3 = "1 2 + 3 *"
        result3 = 9.0
        test4 = "1 2 3 4 10 * + + -"
        result4 = -1.0
        test5 = "3 3 / 3 +"
        result5 = 4
        self.assertAlmostEqual(postfix_calc(test1), result1)
        self.assertAlmostEqual(postfix_calc(test2), result2)
        self.assertAlmostEqual(postfix_calc(test3), result3)
        self.assertAlmostEqual(postfix_calc(test4), result4)
        self.assertAlmostEqual(postfix_calc(test5), result5)


if __name__ == '__main__':
    unittest.main()