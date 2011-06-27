'''
Created on May 8, 2009

@author: ben
'''
import unittest
import KataTwo

class Test(unittest.TestCase):

    def test_chopIterative(self):
        self.assertEqual(-1, KataTwo.chopIterative(3, []))
        self.assertEqual(-1, KataTwo.chopIterative(3, [1]))
        self.assertEqual(0, KataTwo.chopIterative(1, [1]))
        #
        self.assertEqual(0, KataTwo.chopIterative(1, [1, 3, 5]))
        self.assertEqual(1, KataTwo.chopIterative(3, [1, 3, 5]))
        self.assertEqual(2, KataTwo.chopIterative(5, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopIterative(0, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopIterative(2, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopIterative(4, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopIterative(6, [1, 3, 5]))
        #
        self.assertEqual(0, KataTwo.chopIterative(1, [1, 3, 5, 7]))
        self.assertEqual(1, KataTwo.chopIterative(3, [1, 3, 5, 7]))
        self.assertEqual(2, KataTwo.chopIterative(5, [1, 3, 5, 7]))
        self.assertEqual(3, KataTwo.chopIterative(7, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopIterative(0, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopIterative(2, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopIterative(4, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopIterative(6, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopIterative(8, [1, 3, 5, 7]))

    def test_chopRecursive(self):
        self.assertEqual(-1, KataTwo.chopRecursive(3, []))
        self.assertEqual(-1, KataTwo.chopRecursive(3, [1]))
        self.assertEqual(0, KataTwo.chopRecursive(1, [1]))
        #
        self.assertEqual(0, KataTwo.chopRecursive(1, [1, 3, 5]))
        self.assertEqual(1, KataTwo.chopRecursive(3, [1, 3, 5]))
        self.assertEqual(2, KataTwo.chopRecursive(5, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopRecursive(0, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopRecursive(2, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopRecursive(4, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopRecursive(6, [1, 3, 5]))
        #
        self.assertEqual(0, KataTwo.chopRecursive(1, [1, 3, 5, 7]))
        self.assertEqual(1, KataTwo.chopRecursive(3, [1, 3, 5, 7]))
        self.assertEqual(2, KataTwo.chopRecursive(5, [1, 3, 5, 7]))
        self.assertEqual(3, KataTwo.chopRecursive(7, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopRecursive(0, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopRecursive(2, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopRecursive(4, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopRecursive(6, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopRecursive(8, [1, 3, 5, 7]))
        
    def test_chopSlice(self):
        self.assertEqual(-1, KataTwo.chopSliceRecursive(3, []))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(3, [1]))
        self.assertEqual(0, KataTwo.chopSliceRecursive(1, [1]))
        #
        self.assertEqual(0, KataTwo.chopSliceRecursive(1, [1, 3, 5]))
        self.assertEqual(1, KataTwo.chopSliceRecursive(3, [1, 3, 5]))
        self.assertEqual(2, KataTwo.chopSliceRecursive(5, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(0, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(2, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(4, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(6, [1, 3, 5]))
        #
        self.assertEqual(0, KataTwo.chopSliceRecursive(1, [1, 3, 5, 7]))
        self.assertEqual(1, KataTwo.chopSliceRecursive(3, [1, 3, 5, 7]))
        self.assertEqual(2, KataTwo.chopSliceRecursive(5, [1, 3, 5, 7]))
        self.assertEqual(3, KataTwo.chopSliceRecursive(7, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(0, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(2, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(4, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(6, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceRecursive(8, [1, 3, 5, 7]))
        
    def test_chopSliceIterative(self):
        self.assertEqual(-1, KataTwo.chopSliceIterative(3, []))
        self.assertEqual(-1, KataTwo.chopSliceIterative(3, [1]))
        self.assertEqual(0, KataTwo.chopSliceIterative(1, [1]))
        #
        self.assertEqual(0, KataTwo.chopSliceIterative(1, [1, 3, 5]))
        self.assertEqual(1, KataTwo.chopSliceIterative(3, [1, 3, 5]))
        self.assertEqual(2, KataTwo.chopSliceIterative(5, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(0, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(2, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(4, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(6, [1, 3, 5]))
        #
        self.assertEqual(0, KataTwo.chopSliceIterative(1, [1, 3, 5, 7]))
        self.assertEqual(1, KataTwo.chopSliceIterative(3, [1, 3, 5, 7]))
        self.assertEqual(2, KataTwo.chopSliceIterative(5, [1, 3, 5, 7]))
        self.assertEqual(3, KataTwo.chopSliceIterative(7, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(0, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(2, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(4, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(6, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chopSliceIterative(8, [1, 3, 5, 7]))
        
    def test_chop(self):
        self.assertEqual(-1, KataTwo.chop(3, []))
        self.assertEqual(-1, KataTwo.chop(3, [1]))
        self.assertEqual(0, KataTwo.chop(1, [1]))
        #
        self.assertEqual(0, KataTwo.chop(1, [1, 3, 5]))
        self.assertEqual(1, KataTwo.chop(3, [1, 3, 5]))
        self.assertEqual(2, KataTwo.chop(5, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chop(0, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chop(2, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chop(4, [1, 3, 5]))
        self.assertEqual(-1, KataTwo.chop(6, [1, 3, 5]))
        #
        self.assertEqual(0, KataTwo.chop(1, [1, 3, 5, 7]))
        self.assertEqual(1, KataTwo.chop(3, [1, 3, 5, 7]))
        self.assertEqual(2, KataTwo.chop(5, [1, 3, 5, 7]))
        self.assertEqual(3, KataTwo.chop(7, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chop(0, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chop(2, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chop(4, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chop(6, [1, 3, 5, 7]))
        self.assertEqual(-1, KataTwo.chop(8, [1, 3, 5, 7]))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
