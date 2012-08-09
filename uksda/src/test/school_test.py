'''
Unit tests for school class.
Created on 8 Aug 2012

@author: Fraser
'''
import unittest
from uksda_core.school import School


class TestSchool(unittest.TestCase):

    def setUp(self):
        self.testSchool = School("", "", "ElectricPink Primary School",
                                 300146, 15406)

    def tearDown(self):
        pass

    def testShouldRenameSchool(self):
        s = "ElectricPink Primary School"
        self.testSchool.setName("", "", "Renamed school")
        self.assertEqual(self.testSchool.Name(), "Renamed school",
                         "Renaming school.")
        self.testSchool.fullName = s

if __name__ == "__main__":
    unittest.main()
    pass
