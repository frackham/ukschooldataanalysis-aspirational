'''
Unit tests for student class.
Created on 8 Aug 2012

@author: Fraser
'''
import unittest
from uksda_core.student import Student


class TestStudent(unittest.TestCase):

    def setUp(self):
        self.testStudent = Student("Jones", "Bob", "MALE", "17th February 1983")

    def tearDown(self):
        #TODO: [e] Destroy Student object?
        pass

    #Change property tests.
    def testShouldChangeForename(self):
        self.testStudent.setForename("James")
        #2 tests...check that Name also returns correct value.
        #TODO: [d] 1 unit test per test function is required, as only 1 picked up by test suite.
        self.assertEqual(self.testStudent.getForename(), "James", "Failed to change student forename.")
        self.assertEqual(self.testStudent.Name(case="Proper", order="Surname, Forename"), "Jones, James", "Failed to return Name correctly after change to student forename.")
        self.testStudent.setForename("Bob")  # Reset.
        self.assertEqual(self.testStudent.getForename(), "Bob", "Failed to change student forename.")
        self.assertEqual(self.testStudent.Name(case="Proper", order="Surname, Forename"), "Jones, Bob", "Failed to return Name correctly after change to student forename.")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
