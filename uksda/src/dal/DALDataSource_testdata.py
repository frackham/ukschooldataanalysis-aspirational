'''
Created on 8 Aug 2012

@author: Fraser
'''
from dal.DALDataSource import DALDataSource


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
        #TODO:[c] Create 1 school with 200 yr11 students.
        #TODO:[e] Update this to create multiple schools and datasets with 1000+ students.
        pass
