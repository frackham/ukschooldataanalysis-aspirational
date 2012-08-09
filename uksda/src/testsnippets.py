'''
Created on 9 Aug 2012

@author: Fraser
'''

class MyClass(object):
    '''
    classdocs
    '''


    def __init__(selfparams):
        '''
        Constructor
        '''



#BLOCK 1: This is how we do analysis processes/packages!
def f1(n): #accepts one argument 
    print("F1:" + str(n))
 
def f2(blank=""): #accepts no arguments 
    print("F2") 
 
FUNCTION_LIST = [(f1, (2)), #each list entry is a tuple containing a function object and a tuple of arguments 
                 (f1, (6)),
                 (f2, (""))] 
 
for f, arg in FUNCTION_LIST: 
    f(arg) 
