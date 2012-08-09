'''
Created on 9 Aug 2012

@author: Fraser
'''
import unittest
from test.school_test import TestSchool
from test.student_test import TestStudent

"""class TestWrapper(unittest.TestCase):
    #HACK: Only needed so that PyUnit picks up test suite.
    UKSDA_TestSuite()
 """


"""def UKSDA_TestSuite():
    #School
    suiteSchool = unittest.TestSuite()
    suiteSchool.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSchool))
    print(suiteSchool)
    #Student
    suiteStudent = unittest.TestLoader().loadTestsFromTestCase(TestStudent)

    allsuites = unittest.TestSuite([suiteSchool, suiteStudent])
    print(allsuites)
    iteratedsuites = []
    for thisSuite in allsuites:
        for thisTest in thisSuite:
            iteratedsuites.append(thisTest)
    print(iteratedsuites)  # HACK: PyUnit not picking up on lists within list of suites, despite unittest documentation using it as an example. 
    return iteratedsuites
"""
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #suite = UKSDA_TestSuite()
    unittest.main()
    pass  # TEMP: TO run all unit tests using pyunit, right click on package folder!
