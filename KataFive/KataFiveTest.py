'''
Created on June 1, 2009

@author: ben
'''
import unittest
from KataFive import BloomFilter

class Test(unittest.TestCase):

    checker = BloomFilter()
    with open('/usr/share/dict/words') as f:
        for word in f:
            checker.insert(word.strip())
    
    def test_contains(self):
        filter = BloomFilter()
        filter.insert("hello")
        self.assertTrue(filter.contains("hello"), 'filter should contain "hello"')
        
    def test_does_not_contains(self):
        filter = BloomFilter()
        filter.insert("world")
        self.assertFalse(filter.contains("hello"), 'filter should not contain "hello"')
       
    def test_spell_checker_contains(self): 
        self.assertTrue(self.checker.contains("hello"), '"hello" should be a word')
        
    def test_spell_checker_does_not_contain(self):
        word = 'bobloblaw'
        self.assertFalse(self.checker.contains(word), '"'+word+'" should not be a word')
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
