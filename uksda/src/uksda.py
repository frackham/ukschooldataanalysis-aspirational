'''
Created on 8 Aug 2012

@author: Fraser
'''
from uksda_importclasses import *
from analysis.schooldescription import * #Temp
from dal.dal import *


class System(object):  # TODO: [c] Check if there is an issue calling this class System!
    '''
    Singleton template?
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
        pass


def development_DoAnalysis():
    print("Doing Development Analysis...")
    #STEPS:
    # 1 Define DAL (test)
    DAL = DataAccessLayer() #Defining without parameters uses testdata by default.
    # 2 Create dataset
    dSource = DAL.DataSource()
    thisDataset = dSource.getDataset()
    # 3 Load dataset with school from DAL,test
    # 4 Do Analysis on dataset
    thisAnalysis = SchoolDescriptionAnalysis(thisDataset)
    # 5 Render Analysis on dataset.
    #temp: print
    print(thisAnalysis)

    print("...done.")

if __name__ == "__main__":
    development_DoAnalysis()
