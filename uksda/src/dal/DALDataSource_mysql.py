'''
Created on 8 Aug 2012

@author: Fraser
'''
from dal.DALDataSource import DALDataSource


class DALDataSource_mysql(DALDataSource):
    '''MySQL data source object.

    ---.'''

    def __init__(self, params):
        '''Constructor for mysql data source. Use params to set up connection. Test connection on first use?

        ---
        '''
        pass

    def __str__(self):
        return("MySQL data source")  # TODO: [d] Add description of connection data.

    #Methods
