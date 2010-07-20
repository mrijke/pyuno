'''
Created on Jul 19, 2010

@author: rupert
'''
from Hand import Hand

class Player(object):
    '''
    Represents a player in the UNO game.
    Can be human, or can be controlled by an AI.
    '''
    
    def __init__(self, name, deck, AI=None):
        '''
        Constructs a new Player
        '''
        self._name = name
        self._AI = AI
        self._hand = Hand()
        self._deck = deck
        initcards = self._deck.draw7Cards()
        for card in initcards:
            self._hand.addCard(card)
            
    def getCurrentHand(self):
        return self._hand.getCards()
    
    def getName(self):
        return self._name
    
    def drawCard(self):
        card = self._deck.drawCard()
        self._hand.addCard(card)
        
    def drawTwoCards(self):
        self.drawCard()
        self.drawCard()
        
    def removeFromHand(self, card):
        self._hand.removeCard(card)