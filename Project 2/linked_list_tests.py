import unittest
from linked_list import *

class song():
    def __init__(self, title, artist, album, number):
        self.title = title
        self.artist = artist
        self.album = album
        self.number = number

    def __repr__ (self):
        return "%s, %s, %s, %s" % (self.title, self.artist, self.album, self.number)

    def __eq__(self, other):
        if isinstance(other, song):
            return self.title == other.title and self.artist == other.artist and self.album  == other.album and self.number == other.number
        else:
            return False


class TestList(unittest.TestCase):
    # Note that this test doesn't assert anything! It just verifies your
    #  class and function definitions.
    def test_interface(self):
        temp_list = empty_list()
        temp_list = add(temp_list, 0, 'Hello!')
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, 'Bye!')
        remove(temp_list, 0)

    def test_pair(self):
        pair0 = Pair(1, Pair(2))
        pair1 = Pair(1, Pair(2))
        pair2 = Pair(1, Pair(3))
        self.assertEqual(repr(pair0), '1, 2, None')
        self.assertTrue(pair0 == pair1)
        self.assertFalse(pair0 == pair2)
        self.assertFalse(pair0 == 'a')

    def test_empty_list(self):
        self.assertEqual(empty_list(), None)

    def test_add(self):
        list0 = None
        list1 = Pair(1, Pair('A', Pair(2)))
        result0 = Pair('Test')
        result1 = Pair(1, Pair('A', Pair('a', Pair(2))))
        result2 = Pair(1, Pair('A', Pair(2, Pair('B'))))
        self.assertEqual(add(list0, 0, 'Test'), result0)
        self.assertEqual(add(list1, 2, 'a'), result1)
        self.assertEqual(add(list1, 3, 'B'), result2)
        self.assertRaises(IndexError, lambda: add(list1, -1, 'Test'))
        self.assertRaises(IndexError, lambda: add(list1, 4, 'Test'))

    def test_length(self):
        list0 = None
        list1 = Pair(1, Pair('A', Pair(2)))
        self.assertEqual(length(list0), 0)
        self.assertEqual(length(list1), 3)

    def test_get(self):
        list0 = None
        list1 = Pair(1, Pair('A', Pair(2)))
        self.assertRaises(IndexError, lambda: get(list0, 0))
        self.assertRaises(IndexError, lambda: get(list1, -1))
        self.assertRaises(IndexError, lambda: get(list1, 3))
        self.assertEqual(get(list1, 0), 1)
        self.assertEqual(get(list1, 1), 'A')
        self.assertEqual(get(list1, 2), 2)

    def test_set(self):
        list0 = None
        list1 = Pair(1, Pair('A', Pair(2)))
        result1 = Pair(1, Pair('A', Pair('a')))
        self.assertRaises(IndexError, lambda: set(list0, 0, 'Test'))
        self.assertEqual(set(list1, 2, 'a'), result1)
        self.assertRaises(IndexError, lambda: add(list1, -1, 'Test'))
        self.assertRaises(IndexError, lambda: add(list1, 4, 'Test'))

    def test_remove(self):
        list0 = None
        list1 = Pair(1, Pair('A', Pair(2)))
        result1 = (2, Pair(1, Pair('A')))
        result2 = ('A', Pair(1, Pair(2)))
        result3 = (1, Pair('A', Pair(2)))
        self.assertRaises(IndexError, lambda: remove(list0, 0))
        self.assertRaises(IndexError, lambda: remove(list0, -1))
        self.assertRaises(IndexError, lambda: remove(list1, -1))
        self.assertRaises(IndexError, lambda: remove(list1, 3))
        self.assertEqual(remove(list1, 2), result1)
        self.assertEqual(remove(list1, 1), result2)
        self.assertEqual(remove(list1, 0), result3)

    def test_foreach(self):
        def func(x):
            if str(x).isalpha():
                return x
            else:
                return x*2
        list0 = None
        list1 = Pair(1, Pair('A', Pair(2)))
        result1 = Pair(2, Pair('A', Pair(4)))
        self.assertIsNone(foreach(list0, func))
        self.assertIsNone(foreach(list1, func))



    def test_find_key(self):
        key0 = 0
        key1 = 1
        key2 = 2
        key3 = 3
        key4 = 4
        result1 = ['number','album','artist','title']
        result2 = ['title','album','artist','number']
        result3 = ['artist','album','title','number']
        result4 = ['album','artist','title','number']
        result5 = None
        self.assertEqual(find_key(key0), result1)
        self.assertEqual(find_key(key1), result2)
        self.assertEqual(find_key(key2), result3)
        self.assertEqual(find_key(key3), result4)
        self.assertEqual(find_key(key4), result5)

    def test_find_least(self):
        order = ['album','artist','title','number']
        song0 = song('Hello', 'World', 'Saying', 0)
        song1 = song('World', 'Eating', 'News', 1)
        song2 = song('Bye', 'Replace','Me', 2)
        song3 = song('Boo', 'Foo', 'Wake', 0)
        song4 = song('Leap', 'Foo', 'Wake', 1)
        song5 = song('Stupid', 'Idiot', 'Wake', 2)
        test0 = Pair(song0,Pair(song1, Pair(song2)))
        test1 = Pair(song3,Pair(song4, Pair(song5)))
        test2 = None
        result1 = 2
        result2 = 0
        result3 = None
        self.assertEqual(find_least(test0,order), result1)
        self.assertEqual(find_least(test1,order), result2)
        self.assertEqual(find_least(test2,order), result3)

    def test_sort(self):
        order = ['album', 'artist', 'title', 'number']
        song0 = song('Hello', 'World', 'Saying', 0)
        song1 = song('World', 'Eating', 'News', 1)
        song2 = song('Bye', 'Replace', 'Me', 2)
        song3 = song('Boo', 'Foo', 'Wake', 0)
        song4 = song('Leap', 'Foo', 'Wake', 1)
        song5 = song('Stupid', 'Idiot', 'Wake', 2)
        test0 = Pair(song0, Pair(song1, Pair(song2)))
        test1 = Pair(song3, Pair(song4, Pair(song5)))
        test2 = None
        result1 = Pair(song2, Pair(song1, Pair(song0)))
        result2 = Pair(song3, Pair(song4, Pair(song5)))
        result3 = None
        self.assertEqual(sort(test0, order,find_least), result1)
        self.assertEqual(sort(test1, order,find_least), result2)
        self.assertEqual(sort(test2, order,find_least), result3)

    def test_song(self):
        song0 = song('1','2','3','4')
        song1 = song('1','2','3','4')
        self.assertEqual(repr(song0), "1, 2, 3, 4")
        self.assertTrue(song0 == song1)
        self.assertFalse(song0 == None)


if __name__ == '__main__':
    unittest.main()
