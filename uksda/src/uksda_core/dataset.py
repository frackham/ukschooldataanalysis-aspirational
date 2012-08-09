'''
Created on 9 Aug 2012

@author: Fraser
'''


class Dataset(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._collection = []

    def append(self, objs):
        try:
            iterator = iter(objs)
        except TypeError:
            self._collection.append(objs)
        else:
            for thing in iterator:
                self._collection.append(thing)
