#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.length() == 0 # should be 0 (empty list)
        assert s.data.length() == 0

    def test_init_with_list(self):
        s = Set(['A', 'B', 'C'])
        assert s.length() == 3  # should have 3 items
        assert s.data.length() == 3

    def test_init_with_list_duplicate_item(self):
        s = Set(['A', 'B', 'B'])
        assert s.length() == 2  # does not add duplicate

    def test_contains(self):
        s = Set(['A','B'])
        assert s.length() == 2
        assert s.contains('A') is True
        assert s.contains('B') is True
        assert s.contains('C') is False
        assert s.contains('') is False # nothing is passed. return False

    def test_add(self):
        s = Set()
        s.add('A')
        assert s.length() == 1
        assert s.contains('A') is True
        s.add('B')
        assert s.length() == 2
        assert s.contains('B') is True
        s.add('C')
        assert s.length() == 3
        assert s.contains('C') is True
        s.add('A') # duplicate
        assert s.length() == 3 # should not add the duplicate

    def test_remove(self):
        s = Set(['A', 'B', 'C'])
        assert s.length() == 3
        s.remove('A')
        assert s.length() == 2  # should have removed 'A'
        with self.assertRaises(KeyError):
            s.remove('A') # not in set

    def test_union(self):
        s = Set(['A', 'B', 'C', 'D'])
        temp = Set(['E', 'F'])
        assert s.union(temp).length() == 6
        temp2 = Set(['A'])
        assert s.union(temp2).length() == 4 # not repeating duplicates

    def test_intersect(self):
        s = Set(['A', 'B', 'C', 'D'])
        temp = Set(['A', 'C'])
        assert s.intersection(temp).length() == 2
        temp2 = Set(['Z'])
        assert s.intersection(temp2).length() == 0 # no intersection

    def test_difference(self):
        s = Set(['A', 'B', 'C'])
        temp = Set(['C', 'D'])
        assert s.difference(temp).length() == 2
        temp2 = s = Set(['A', 'B', 'C'])
        assert s.difference(temp2).length() == 0 # no difference

    def test_is_subset(self):
        s = Set(['A', 'B', 'C'])
        temp = Set(['A', 'B'])
        assert temp.is_subset(s) is True
        temp2 = Set(['E','F'])
        assert temp2.is_subset(s) is False


if __name__ == '__main__':
    unittest.main()
