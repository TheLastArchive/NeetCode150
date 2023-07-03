import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Arrays_and_Hashing.top_k_frequent_elements as aah

class TestTopKFrequent(unittest.TestCase):
    def test_correct(self):
        solution = aah.Solution()
        self.assertEqual(solution.topKFrequent([1,1,1,2,2,3], 2), [1,2])
        self.assertEqual(solution.topKFrequent([1], 1), [1])
        

if __name__ == '__main__':
    unittest.main()