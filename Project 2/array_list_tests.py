import unittest
from array_list import *
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
        temp_list = add(temp_list, 0, "Hello!")
        length(temp_list)
        get(temp_list, 0)
        temp_list = set(temp_list, 0, "Bye!")
        remove(temp_list, 0)

    def test_List(self):
        self.assertEqual(repr(List(2, ['a', 'b'])), "['a', 'b'] | Length: 2 | Capacity: 2")
        self.assertTrue(List(2, ['a', 'b']) == List(2, ['a', 'b']))
        self.assertFalse(List(2, ['a', 'b']) == List(1, ['a']))
        self.assertFalse(List(2, ['a', 'b']) == 'a')

    def test_empty_list(self):
        self.assertEqual(empty_list(), List())

    def test_add(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        result0 = List(1, ['a'])
        result05 = List(2, ['a', 'b'])
        result1 = List(4, ['a', 'b', 'c', 'd'])
        result2 = List(4, ['d', 'a', 'b', 'c'])
        result3 = List(4, ['a', 'b', 'd', 'c'])
        self.assertEqual(add(list0, 0, 'a'), result0)
        self.assertEqual(add(add(list0, 0, 'a'), 1, 'b'), result05)
        self.assertEqual(add(list1, 3, 'd'), result1)
        self.assertEqual(add(list1, 0, 'd'), result2)
        self.assertEqual(add(list1, 2, 'd'), result3)
        self.assertRaises(IndexError, lambda: add(list0, -1, 'a'))
        self.assertRaises(IndexError, lambda: add(list1, 4, 'a'))
        tester = add(add(empty_list(), 0, None), 1, 4)
        self.assertEqual(tester, List(2, [None, 4]))

    def test_length(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        self.assertEqual(length(list0), 0)
        self.assertEqual(length(list1), 3)

    def test_get(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        self.assertRaises(IndexError, lambda: get(list0, 0))
        self.assertRaises(IndexError, lambda: get(list1, -1))
        self.assertRaises(IndexError, lambda: get(list1, 4))
        self.assertEqual(get(list1, 0), 'a')
        self.assertEqual(get(list1, 1), 'b')
        self.assertEqual(get(list1, 2), 'c')

    def test_set(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        result1 = List(3, ['d', 'b', 'c'])
        result2 = List(3, ['a', 'd', 'c'])
        result3 = List(3, ['a', 'b', 'd'])
        self.assertRaises(IndexError, lambda: set(list0, 0, 'a'))
        self.assertRaises(IndexError, lambda: set(list1, -1, 'a'))
        self.assertRaises(IndexError, lambda: set(list1, 3, 'a'))
        self.assertEqual(set(list1, 0, 'd'), result1)
        self.assertEqual(set(list1, 1, 'd'), result2)
        self.assertEqual(set(list1, 2, 'd'), result3)

    def test_remove(self):
        list0 = None
        list1 = List(3, ['a', 'b', 'c'])
        list2 = List(1, ['a'])
        result1 = ('a', List(2, ['b', 'c']))
        result2 = ('b', List(2, ['a', 'c']))
        result3 = ('c', List(2, ['a', 'b']))
        result4 = ('a', None)
        self.assertRaises(IndexError, lambda: remove(list0, 0))
        self.assertRaises(IndexError, lambda: remove(list1, -1))
        self.assertRaises(IndexError, lambda: remove(list1, 3))
        self.assertRaises(IndexError, lambda: remove(list2, 1))
        self.assertEqual(remove(list1, 0), result1)
        self.assertEqual(remove(list1, 1), result2)
        self.assertEqual(remove(list1, 2), result3)
        self.assertEqual(remove(list2, 0), result4)

    def test_foreach(self):
        def func(x):
            if str(x).isalpha():
                return x
            else:
                return x*2
        list0 = empty_list()
        list1 = List(3,[1,'A',2])
        result1 = List(3,[2,'A',4])
        self.assertEqual(foreach(list0, func), None)
        self.assertEqual(foreach(list1, func), None)
        self.assertEqual(list0, empty_list())
        self.assertEqual(list1, result1)

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
        test0 = List(3,[song0, song1, song2])
        test1 = List(3,[song3, song4, song5])
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
        test0 = List(3, [song0, song1, song2])
        test1 = List(3, [song3, song4, song5])
        test2 = None
        result1 = List(3, [song2, song1, song0])
        result2 = List(3, [song3, song4, song5])
        self.assertEqual(sort(test0, order, find_least), result1)
        self.assertEqual(sort(test1, order, find_least), result2)
        self.assertEqual(sort(test2, order, find_least), None)


    def test_song(self):
        song0 = song('1','2','3','4')
        song1 = song('1','2','3','4')
        self.assertEqual(repr(song0), "1, 2, 3, 4")
        self.assertTrue(song0 == song1)
        self.assertFalse(song0 == None)

if __name__ == '__main__':
    unittest.main()
