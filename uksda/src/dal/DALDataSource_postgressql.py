'''
Created on 8 Aug 2012

@author: Fraser
'''
from dal.DALDataSource import DALDataSource


class DALDataSource_postgressql(DALDataSource):
    '''postgressql data source object.

    ---.'''

    def __init__(self, params):
        '''Constructor for postgressql data source. Use params to set up connection. Test connection on first use?

        ---
        '''
        pass

    def __str__(self):
        return("postgressql data source") #TODO: [d] Add description of connection data.

    #Methods
