'''
Created on 8 Aug 2012

@author: Fraser
'''
from dal.DALDataSource import *
from uksda_importclasses import *

class DALDataSource_testdata(DALDataSource):
    '''Test data source object.

    Used as default data source if no other data source is defined in DAL.
    Directly returns objects.'''

    def __init__(self):
        '''Constructor for test data.

        This should set up the data here.
        '''
        self.createData()

    def __str__(self):
        return("Testdata data source")

    #Methods.
    def createData(self):
        # TODO:[c] Create 1 school with 200 yr11 students.
        # TODO:[e] Update this to create multiple schools and datasets with 1000+ students.
        print("Test data data source creating school...")
        self.testSchool = School("EPS", "Electric Pink Primary", "Electric Pink Primary School",
                            99999, 99999, "NW1 1AA", "1 Church Street, Wimbledon, London")
        #TODO: [c]Gen students here.
        print("...done.")

    def getDataset(self):
        """Returns the default test dataset."""
        d = Dataset()
        d.append(self.testSchool)
        return d
