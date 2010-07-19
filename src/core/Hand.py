'''
Created on Jul 19, 2010

@author: rupert
'''

class Hand(object):
    '''
    Represents a Hand of cards held by a Player
    '''


    def __init__(self):
        '''
        Constructs a new Hand
        '''
        self._cards = []
        
    def remove_card(self, targetcard):
        for card in self._cards:
            if (card.getColor() == targetcard.getColor() and card.getData() == targetcard.getData()):
                self._cards.remove(targetcard)
                return True
        return False