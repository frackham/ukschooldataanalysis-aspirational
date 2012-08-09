'''
Data Access Layer

Created on 8 Aug 2012

@author: Fraser
'''
from dal.DALDataSource import DALDataSource
#TODO: [e] Not needed? Imported by each of the inherited classes...
from dal.DALDataSource_testdata import DALDataSource_testdata
from dal.DALDataSource_flatfiles import DALDataSource_flatfiles
from dal.DALDataSource_mysql import DALDataSource_mysql
from dal.DALDataSource_postgressql import DALDataSource_postgressql


class DataAccessLayer(object):
    '''
    classdocs
    '''
    defaultDataSource = DALDataSource_testdata()

    def __init__(self, dataSource=defaultDataSource):
        '''Initialises DAL object. dataSource defaults to test data.

        '''
        self.setDataSource(dataSource)
        print("DAL initialised using " + str(dataSource))

    def setDataSource(self, dataSource):
        print("Data source set")  # TODO: [e] Replace with logging.
        self.dataSource = dataSource

    def getDataSource(self):
        print("getDataSource")
        return self.dataSource

    def DataSource(self):
        print("DataSource, now calling getDataSource.")
        return self.getDataSource()
