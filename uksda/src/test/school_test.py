'''
Unit tests for school class.
Created on 8 Aug 2012

@author: Fraser
'''
import unittest
from uksda_core.school import School

class TestSchool(unittest.TestCase):

    def setUp(self):
        self.testSchool = School()

    def tearDown(self):
        pass

    def testShouldRenameSchool(self):
        self.testSchool.setName("Renamed school")
        #TODO: WRITE TEST!

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
