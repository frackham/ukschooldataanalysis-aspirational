'''
Created on 9 Aug 2012

@author: Fraser
'''


class School(object):
    '''Core object representing a single school.

TODO: A fair bit!'''

    def __init__(self, initials, shortName, fullName,
                 dfeID, centreID,
                 postcode="", addressblock=""):
        self.setName(initials, shortName, fullName)
        self.setDfeID(dfeID)
        self.setCentreID(centreID)


    def __str__(self,):
        return "School: " + self.Name() + ": Dfe:" + self.getDfeID() + ", CentreID:" + self.getCentreID()

    #Properties (set).
    def setName(self, initials, shortName, fullName):
        #Fullname only.
        self.fullName = fullName
        self.shortName = fullName
        chars = [c[0:1] for c in fullName.split(" ")]
        s = "".join(chars)
        self.initials = s

    def setDfeID(self, dfeID):
        self.dfeID = dfeID

    def setCentreID(self, centreID):
        self.centreID = centreID

    #Properties (get).
    def getName(self):
        return self.fullName

    def getDfeID(self):
        return self.dfeID

    def getCentreID(self):
        return self.centreID

    #Properties (readonly).
    def Name(self):
        return self.getName()
