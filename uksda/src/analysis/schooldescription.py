'''
Created on 9 Aug 2012

@author: Fraser
'''

from analysis.base_analysis import BaseAnalysis


class SchoolDescriptionAnalysis(BaseAnalysis):
    '''
    classdocs
    '''


    def __init__(self, dataset):
        '''
        Constructor <-- needed? Use default, which should define how it checks prerequisites.
        '''
        self.model = dataset
        # TODO: [c] This is where the analysis must test prerequisites, and whether the *object(s)* passed meet prereqs.
        pass

    def __str__(self):
        s = "School Description analysis representation goes here."
        s += "\n"
        return (s)
