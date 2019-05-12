#!python

from set import Set
import unittest

class SetTest(unittest.TestCase):

    def test_init(self):
        s = Set()
        assert s.length() == 0 # should be 0 (empty list)
        assert s.data.length() == 0
        assert s.size == 0

    def test_init_with_list(self):
        s = Set(['Ab', 'Bc', 'Cd'])
        assert s.length() == 3  # should have 3 items
        assert s.data.length() == 3
        assert s.size == 3

    def test_init_with_list_duplicate_item(self):
        s = Set(['Ab', 'Bc', 'Bc'])
        assert s.length() == 2  # does not add duplicate
        assert s.size == 2

    def test_contains(self):
        s = Set(['Ab','Bc'])
        assert s.length() == 2
        assert s.size == 2
        assert s.contains('Ab') is True
        assert s.contains('Bc') is True
        assert s.contains('Cd') is False
        assert s.contains('') is False # nothing is passed. return False

    def test_add(self):
        s = Set()
        s.add('Ab')
        assert s.length() == 1
        assert s.size == 1
        assert s.contains('Ab') is True
        s.add('Bc')
        assert s.length() == 2
        assert s.size == 2
        assert s.contains('Bc') is True
        s.add('Cd')
        assert s.length() == 3
        assert s.size == 3
        assert s.contains('Cd') is True
        s.add('Ab') # duplicate
        assert s.length() == 3 # should not add the duplicate
        assert s.size == 3

    def test_remove(self):
        s = Set(['Ab', 'Bc', 'C'])
        assert s.length() == 3
        assert s.size == 3
        s.remove('Ab')
        assert s.length() == 2  # should have removed 'A'
        assert s.size == 2
        with self.assertRaises(KeyError):
            s.remove('Ab') # not in set

    def test_union(self):
        s = Set(['Ab', 'Bc', 'C', 'D'])
        temp = Set(['E', 'F'])
        assert s.union(temp).length() == 6
        assert s.union(temp).size == 6
        temp2 = Set(['Ab'])
        assert s.union(temp2).length() == 4 # not repeating duplicates
        assert s.union(temp2).size == 4

    def test_intersect(self):
        s = Set(['Ab', 'Bc', 'Cd', 'De'])
        temp = Set(['Ab', 'Cd'])
        assert s.intersection(temp).length() == 2
        assert s.intersection(temp).size == 2
        temp2 = Set(['Z'])
        assert s.intersection(temp2).length() == 0 # no intersection
        assert s.intersection(temp2).size == 0

    def test_difference(self):
        s = Set(['Aa', 'Bc', 'Cd'])
        temp = Set(['Cd', 'De'])
        assert s.difference(temp).length() == 2
        assert s.difference(temp).size == 2
        temp2 = s = Set(['Ab', 'Bc', 'Cd'])
        assert s.difference(temp2).length() == 0 # no difference
        assert s.difference(temp2).size == 0

    def test_is_subset(self):
        s = Set(['Ab', 'Bc', 'Cd'])
        temp = Set(['Ab', 'Bc'])
        assert temp.is_subset(s) is True
        temp2 = Set(['Ef','F'])
        assert temp2.is_subset(s) is False


if __name__ == '__main__':
    unittest.main()
