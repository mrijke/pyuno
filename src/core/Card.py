'''
Created on Apr 15, 2010

@author: rupert
'''

class Card(object):
    '''
    Represents a single UNO card.
    Properties include: color, number or special ability.
    '''

    def __init__(self, color, data):
        '''
        Constructs a new card.
        '''
        self._color = color
        self._data = data
    
    def getColor(self):
        return self._color
    
    def getData(self):
        return self._data
    
    def isSpecial(self):
        return type(self._data) == type("")
                
    def __str__(self):
        return self._color + " " + str(self._data)