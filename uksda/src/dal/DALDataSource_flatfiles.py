'''
Created on 8 Aug 2012

@author: Fraser
'''
from dal.DALDataSource import DALDataSource


class DALDataSource_flatfiles(DALDataSource):
    '''Flat files data source object.

    ---'''

    def __init__(self, params):
        '''Constructor for flat files data source. Use params to set up path(s). Test path on first use?

        ---
        '''
        pass

    def __str__(self):
        return("Flatfiles data source") #TODO: [d] Add description of path data.

    #Methods
