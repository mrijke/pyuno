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
    
    def addCard(self, card):
        ''' Add a card to the Player's hand '''
        self._cards.append(card)
        
    def getCards(self):
        ''' Return a list of cards currently held in this Hand '''
        return self._cards
    
    def hasCard(self, targetcard):
        ''' Returns true if the targetcard is in this Hand '''
        for card in self._cards:
            if (card.getColor() == targetcard.getColor() and card.getData() == targetcard.getData()):
                return True
        return False
    
    def removeCard(self, targetcard):
        ''' Remove the targetcard from this hand. Returns False if the card is not in this Hand '''
        if self.hasCard(targetcard):
            self._cards.remove(targetcard)
            return True
        return False