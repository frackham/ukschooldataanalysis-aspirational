'''
Created on 8 Aug 2012

@author: Fraser
'''
#TODO: [e] Pretty sure that this is going to need to import the uksda-core core data classes (student, staff, school).
from uksda_core.dataset import Dataset

class DALDataSource(object):
    '''Template object inherited by specific data sources. DO NOT use directly.

    Any common functions/properties go here (may be overridden by inherited
classes).
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        pass

    def __str__(self):
        return("Undefined data source type (base DALDataSource class).")
