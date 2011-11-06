'''
Created on Jul 19, 2010

@author: rupert
'''
from Hand import Hand
from Card import Card

class Player(object):
    '''
    Represents a player in the UNO game.
    Can be human, or can be controlled by an AI.
    '''
    
    def __init__(self, name, initcards):
        '''
        Constructs a new Player
        '''
        self._name = name
        self._hand = Hand()
        for card in initcards:
            self._hand.addCard(card)
            
    def getCurrentHand(self):
        ''' Returns the current set of cards in the Players hand. '''
        return self._hand.getCards()
    
    def testMove(self, current, card):
        ''' Test if playing card with the current card current is a valid move '''
        if card.isWild(): 
            #may always be played, however WD4 requires player to not have current color
            if card.getData() == "wild draw four" and self.hasCardsOfColor(current.getColor()):
                return False
            return True
        if card.getColor() == current.getColor() or card.getData() == current.getData():
            return True
        else:
            return False
    
    def hasCardsOfColor(self, color):
        for card in self._hand.getCards():
            if card.getColor() == color:
                return True
    
    def getPlayableCards(self, current):
        ''' Return a list of cards that are valid moves'''
        res = []
        for card in self._hand.getCards():
            if self.testMove(current, card): res.append(card)
        return res
    
    def getName(self):
        ''' Returns name of player '''
        return self._name
    
    def giveCard(self, cards):
        ''' Add card(s) to the player's hand '''
        if isinstance(cards, Card):
            self._hand.addCard(cards)
        else:
            for card in cards:
                self._hand.addCard(card)
        
    def removeFromHand(self, card):
        ''' Remove given card from player's hand '''
        self._hand.removeCard(card)
