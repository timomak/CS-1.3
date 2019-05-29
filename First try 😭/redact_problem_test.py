#!python

from redact_problem import reduct_words
import unittest


class Redact_Problem_Test(unittest.TestCase):
    def test_base_functionality(self):
        # Check that the code is working for its main purpose without corner cases.
        # This test is from Jake. He showed me hwo sets work.
        assert set(reduct_words([1,2,3,4,5,10], [1,2,3,4,5,6,7,8,9,0])) == set([10])
        assert set(reduct_words(["I", "am", "not", "cool"], ["not"])) == set(["I", "am", "cool"])

    def test_corner_cases(self):
        # Check that it can pass some basic corner cases
        assert set(reduct_words([],[])) == set([])
        assert set(reduct_words()) == set([])
        assert set(reduct_words(["hello"], [1])) == set(["hello"])



if __name__ == '__main__':
    unittest.main()
