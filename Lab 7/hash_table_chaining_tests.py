from hash_table_chaining import *
import unittest


class TestQueue(unittest.TestCase):

    def test_Hashtable(self):
        table1 = Hashtable(None, 0, 8)
        table2 = Hashtable(None, 0, 8)
        self.assertEqual(repr(table1), '[[], [], [], [], [], [], [], []], 0, 8, 0')
        self.assertTrue(table1 == table2)
        self.assertFalse(table2 == None)

    def test_empty_hash_table(self):
        hash = [[], [], [], [], [], [], [], []]
        self.assertEqual(empty_hash_table(), Hashtable(hash, 0, 8))

    def test_get(self):
        hash = [[(0, 'Item1'), (8, 'Item2') ],[(9, 'Item3')], [], [], [], [], [], []]
        table1 = Hashtable(hash, 3, 8, 1)
        table2 = None
        self.assertEqual(get(table1, 8), 'Item2')
        self.assertEqual(get(table1, 9), 'Item3')
        self.assertRaises(LookupError, lambda: get(table1, 16))
        self.assertRaises(LookupError, lambda: get(table2, 8))



    def test_remove(self):
        hash = [[(0, 'Item1'), (8, 'Item2')], [(9, 'Item3')], [], [], [], [], [], []]
        hash2 = [[(0, 'Item1')], [(9, 'Item3')], [], [], [], [], [], []]
        hash3 = [[(0, 'Item1')], [], [], [], [], [], [], []]
        table1 = Hashtable(hash, 3, 8, 1)
        table2 = Hashtable(hash2, 2, 8, 1)
        table3 = Hashtable(hash3, 1, 8, 1)
        table4 = None
        self.assertEqual(remove(table1, 8), table2)
        self.assertEqual(remove(table2, 9), table3)
        self.assertRaises(LookupError, lambda: remove(table1, 16))
        self.assertRaises(LookupError, lambda: remove(table4, 16))


    def test_size(self):
        hash = [[(0, 'Item1'), (8, 'Item2')], [(9, 'Item3')], [], [], [], [], [], []]
        table1 = Hashtable(hash, 3, 8, 1)
        self.assertEqual(size(table1), 3)
        self.assertEqual(size(None), None)


    def test_load_factor(self):
        hash = [[(0, 'Item1'), (8, 'Item2')], [(9, 'Item3')], [], [], [], [], [], []]
        hash2 = [[(0, 'Item1')], [(9, 'Item3')], [], [], [], [], [], []]
        hash3 = [[(0, 'Item1')], [], [], [], [], [], [], []]
        table1 = Hashtable(hash, 3, 8, 1)
        table2 = Hashtable(hash2, 2, 8, 1)
        table3 = Hashtable(hash3, 1, 8, 1)
        self.assertEqual(load_factor(table1), 0.375)
        self.assertEqual(load_factor(table2), 0.25)
        self.assertEqual(load_factor(table3), 0.125)
        self.assertEqual(load_factor(None), 0)


    def test_insert(self):
        table1 = empty_hash_table()
        table2 = Hashtable([[(0,'Item1')], [], [], [], [], [], [], []], 1, 8)
        table3 = Hashtable([[(0,'Item1')], [(1,'Item2')], [], [], [], [], [], []], 2, 8)
        table4 = Hashtable([[(0,'Item1')], [(1,'Item2')], [(2, 'Item3')], [], [], [], [], []], 3, 8)
        table5 = Hashtable([[(0,'Item1')], [(1,'Item2')], [(2, 'Item3')], [(3, 'Item4')], [], [], [], []], 4, 8)
        table6 = Hashtable([[(0,'Item1')], [(1,'Item2')], [(2, 'Item3')], [(3, 'Item4')], [(4, 'Item5')], [], [], []], 5, 8)
        table7 = Hashtable([[(0,'Item1')], [(1,'Item2')], [(2, 'Item3')], [(3, 'Item4')], [(4, 'Item5')], [(5, 'Item6')], [], []], 6, 8)
        table8 = Hashtable([[(0,'Item1')], [(1,'Item2')], [(2, 'Item3')], [(3, 'Item4')], [(4, 'Item5')], [(5, 'Item6')], [(6, 'Item7')], []], 7, 8)
        table9 = Hashtable([[(0,'Item1')], [(1,'Item2')], [(2, 'Item3')], [(3, 'Item4')], [(4, 'Item5')], [(5, 'Item6')], [(6, 'Item7')], [(7, 'Item8')]], 8, 8)
        table10 = Hashtable([[(0, 'Item1'), (8, 'Item9')], [(1, 'Item2')], [(2, 'Item3')], [(3, 'Item4')], [(4, 'Item5')], [(5, 'Item6')],[(6, 'Item7')], [(7, 'Item8')]], 9, 8, 0)
        table11 = Hashtable([[(0, 'Item1'), (8, 'Item9')], [(1, 'Item2'), (9, 'Item10')], [(2, 'Item3')], [(3, 'Item4')], [(4, 'Item5')], [(5, 'Item6')],[(6, 'Item7')], [(7, 'Item8')]], 10, 8, 0)
        table12 = Hashtable([[(0, 'Item1'), (8, 'Item9')], [(1, 'Item2'), (9, 'Item10')], [(2, 'Item3'), (10, 'Item11')], [(3, 'Item4')], [(4, 'Item5')], [(5, 'Item6')],[(6, 'Item7')], [(7, 'Item8')]], 11, 8, 0)
        table13 = Hashtable([[(0, 'Item1')], [(1, 'Item2')], [(2, 'Item3')], [(3, 'Item4')], [(4, 'Item5')], [(5, 'Item6')],[(6, 'Item7')], [(7, 'Item8')], [(8, 'Item9')], [(9, 'Item10')], [(10, 'Item11')], [(11, 'Item12')], [], [], [], []], 12, 16, 0)
        table14 = Hashtable([[(0, 'Item1')], [], [], [], [], [], [], []], 1, 8)
        table15 = Hashtable([[(0, 'Item3')], [], [], [], [], [], [], []], 1, 8, 1)
        self.assertEqual(insert(table1, 0, 'Item1'), table2)
        self.assertEqual(insert(table2, 1, 'Item2'), table3)
        self.assertEqual(insert(table3, 2, 'Item3'), table4)
        self.assertEqual(insert(table4, 3, 'Item4'), table5)
        self.assertEqual(insert(table5, 4, 'Item5'), table6)
        self.assertEqual(insert(table6, 5, 'Item6'), table7)
        self.assertEqual(insert(table7, 6, 'Item7'), table8)
        self.assertEqual(insert(table8, 7, 'Item8'), table9)
        self.assertEqual(insert(table9, 8, 'Item9'), table10)
        self.assertEqual(insert(table10, 9, 'Item10'), table11)
        self.assertEqual(insert(table11, 10, 'Item11'), table12)
        self.assertEqual(insert(table12, 11, 'Item12'), table13)
        self.assertEqual(insert(table14, 0, 'Item3'), table15)
        self.assertEqual(insert(None, 0 , 'Item1'), None)


    def test_collisions(self):
        table1 = empty_hash_table()
        table2 = Hashtable([[(0, 'Item1'), (8, 'Item9')], [(1, 'Item2')], [(2, 'Item3')], [(3, 'Item4')], [(4, 'Item5')], [(5, 'Item6')], [(6, 'Item7')], [(7, 'Item8')]], 9, 8, 0)
        self.assertEqual(collisions(table1), 0)
        self.assertEqual(collisions(None), None)
        self.assertEqual(collisions(table2), 1)


if __name__ == "__main__":
    unittest.main()
