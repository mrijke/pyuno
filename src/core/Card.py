'''
Created on Apr 15, 2010

@author: rupert
'''

class Card(object):
    '''
    Represents a single UNO card.
    Properties include: color and card data (number or special ability).
    '''

    def __init__(self, color, data):
        '''
        Constructs a new card.
        '''
        self._color = color
        self._data = data
    
    def getColor(self):
        ''' Returns the color of the card '''
        return self._color
    
    def getData(self):
        ''' Returns the data of the card (number or special ability) '''
        return self._data
    
    def isSpecial(self):
        ''' Returns true if this card is special (i.e. the self._data attribute is a string) '''
        return type(self._data) == type("")
                
    def __str__(self):
        ''' Returns a string representation of the card displaying the color and the data '''
        return "%s %s" % (self._color, str(self._data))