'''
Created on Apr 23, 2010

@author: rupert
'''
from Deck import Deck
from Player import Player

class Game(object):
    '''
    This represents a game of UNO. It keeps track of a list of the players currently involved in the game.
    '''

    def __init__(self):
        self._playerList = []
        self._deck = Deck()
        self._deck.shuffle()
        self._game_finished = False
        self._currentPlayer = 0
        self._currentCard = self._deck.drawCard()
    
    def getDeck(self):
        return self._deck
    
    def addPlayerToGame(self, name, AI):
        self._playerList.append(Player(name, self._deck, AI))
    
    def getCurrentCard(self):
        return self._currentCard
    
    def isFinished(self):
        return self._game_finished
    
    def testMove(self, card):
        if card.isSpecial():
            #only the colors need to match now
            if card.getColor() == self._currentCard.getColor(): 
                return True
            return False
        if card.getColor() == self._currentCard.getColor():
            return True
        else:
            if card.getData() == self._currentCard.getData():
                return True
            return False
        
    def doMove(self, player, card):
        if self.testMove(card):
            player.removeFromHand(card)
            self._currentCard = card
            return True
        return False
    
    def nextPlayer(self):
        res = self._playerList[self._currentPlayer]
        self._currentPlayer += 1
        if self._currentPlayer >= len(self._playerList):
            self._currentPlayer = 0 
        return res
                
        