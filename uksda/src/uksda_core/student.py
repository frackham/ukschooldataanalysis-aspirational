'''
Created on 6 Aug 2012

@author: Fraser
'''


class Student(object):
    '''Core object representing a single student.

TODO: A fair bit!'''


    def __init__(self, surname, forename, gender, dob):
        '''Constructor for student class.

Requires surname, forename, gender and dateofbirth values.
Gender accepts any usual string indicator for gender (M, Male, Man, Boy, B), regardless of case.
        '''
        #TODO: [e] Pull student from local version.
        self.setSurname(surname) 
        self.setForename(forename)
        self.setGender(gender)
        self.setDOB(dob) #DOB = Date of birth.

    #Properties (set)
    def setSurname(self, surname):
        self.surname = surname

    def setForename(self, forename):
        self.forename = forename

    def setGender(self, gender):
        """Gender accepts any usual string indicator for gender (M, Male, Man, Boy, B), regardless of case.

        """
        self.gender = gender

    def setDOB(self, dob):
        #TODO: [e] handle various formats of dob.
        self.dob = dob

    #Properties (get). Using get/set properties in order to keep a single point of processing on properties (e.g. if I want to change how DOBs are handled, we never use self.dob but instead change it once in self.getDOB().) 
    def getSurname(self):
        return self.surname

    def getForename(self):
        return self.forename

    def getGender(self):
        return self.gender

    def getDOB(self):
        return self.dob

    #Properties (get aliases)
    def DOB(self):
        return self.getDOB()  # TODO: [c] Is this the best way of doing this?

    #Properties (readonly)
    def Name(self, case="Proper", order="Surname, Forename"):
        """
        """
        # TODO: [i] Inherit from system settings?
        return self.getSurname() + ", " + self.getForename()
