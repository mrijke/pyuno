'''
Created on Apr 23, 2010

@author: rupert
'''
from Deck import Deck
from Player import Player

class InvalidMoveException(Exception):
    pass

class Game(object):
    '''
    This represents a game of UNO. It keeps track of a list of the players currently involved in the game.
    '''

    def __init__(self):
        self._playerList = []
        self._deck = Deck()
        self._deck.shuffle()
        self._currentPlayer = 0
        self._currentCard = self._deck.drawCard()
    
    def getDeck(self):
        return self._deck
    
    def addPlayerToGame(self, name, AI):
        self._playerList.append(Player(name, self._deck, AI))
    
    def getCurrentCard(self):
        return self._currentCard
    
    def isFinished(self):
        for player in self._playerList:
            if len(player.getCurrentHand()) == 0:
                return True
        return False
    
    def testMove(self, card):
        if card.getColor() == self._currentCard.getColor():
            return True
        else:
            if card.getData() == self._currentCard.getData():
                return True
            raise InvalidMoveException
        
    def hasUno(self, player):
        return len(player.getCurrentHand()) == 1
        
    def applySpecial(self,card):
        ability = card.getData()
        if ability == 'skip':
            self._currentPlayer+=1
            if self._currentPlayer >= len(self._playerList):
                self._currentPlayer = 0
            return True
        elif ability == 'reverse':
            self._playerList = self._playerList[::-1] #reverse the list
            self._currentPlayer = abs(self._currentPlayer-len(self._playerList)) #fix order
            if self._currentPlayer > len(self._playerList)-1:
                self._currentPlayer = 0
            return False
        elif ability == 'draw 2':
            try:
                self._playerList[self._currentPlayer+1].drawTwoCards()
                self._currentPlayer+=1
            except:
                self._playerList[0].drawTwoCards()
                self._currentPlayer = 0
            return True
        
    def doMove(self, player, card):
        self.testMove(card)
        nextPlayer = True
        if card.isSpecial(): nextPlayer = self.applySpecial(card)
        player.removeFromHand(card)
        self._currentCard = card
        if nextPlayer:
            self._currentPlayer += 1
            if self._currentPlayer >= len(self._playerList):
                self._currentPlayer = 0        
        
    def currentPlayer(self):
        return self._playerList[self._currentPlayer] 
    
    def getNextPlayerName(self):
        try:
            return self._playerList[self._currentPlayer-1].getName()
        except IndexError:
            return self._playerList[self._currentPlayer].getName()
        
    def playerPasses(self):
        self._currentPlayer += 1
        if self._currentPlayer >= len(self._playerList):
            self._currentPlayer = 0
     
        