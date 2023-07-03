import unittest
#I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS I HATE PYTHON IMPORTS
import os
import sys
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
root = os.path.dirname(parent)
sys.path.append(root)
import Arrays_and_Hashing.group_anagrams as aah

class TestContainsDuplicates(unittest.TestCase):
    def test_correct(self):
        solution = aah.Solution()
        expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
        values = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        self.compare_output(expected, values)
        
        expected = [[""]]
        values = solution.groupAnagrams([""])
        self.compare_output(expected, values)
        
        expected = [["a"]]
        values = solution.groupAnagrams(["a"])
        self.compare_output(expected, values)
    
    
    """
    Compares the given arrays and the expected arrays.
    Since the arrays are within arrays, a simple assertion will not work due
    to the unordered outputs
    """
    def compare_output(self, expected, values):
        for value in values:
            if sorted(value) not in expected:
                self.fail(f"""Incorrect value.\n{value} not in expected values: {expected}""")
        

if __name__ == '__main__':
    unittest.main()