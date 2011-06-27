'''
Created on May 15, 2009

@author: ben
'''
import unittest
import KataFour

class Test(unittest.TestCase):

    def test_weather(self):
        self.assertEqual('14', KataFour.smallestTempSpread())
        
    def test_football(self):
        self.assertEqual('Aston_Villa', KataFour.smallestScoreSpread())
    
    def test_weather_refactor(self):
        self.assertEqual('14', KataFour.smallestTempRefactor())
        
    def test_football_refactor(self):
        self.assertEqual('Aston_Villa', KataFour.smallestScoreRefactor())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
