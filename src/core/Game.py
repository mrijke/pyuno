'''
Created on Apr 23, 2010

@author: rupert
'''
from Deck import Deck
from Card import Card
from Player import Player
from AIPlayer import AIPlayer

class InvalidMoveException(Exception):
    pass

class Game(object):
    '''
    This represents a game of UNO. It keeps track of a list of the players currently involved in the game.
    '''

    def __init__(self):
        ''' Creates a new Game. '''
        self._playerList = []
        self._deck = Deck()
        self._deck.shuffle()
        self._currentPlayer = 0
        self._currentCard = self._deck.drawCard()
        self._blankCards = {
                'blue' : Card('blue', 'blank'),
                'yellow' : Card('yellow', 'blank'),
                'red'    : Card('red', 'blank'),
                'green'  : Card('green', 'blank')}
            
    def getDeck(self):
        ''' Returns the deck used for this game '''
        return self._deck
    
    def addPlayerToGame(self, name):
        ''' Add a human player to the game '''
        self._playerList.append(Player(name, self._deck))
        
    def addAIPlayerToGame(self, name):
        ''' Add an AI player to the game '''
        self._playerList.append(AIPlayer(name, self._deck))
    
    def getCurrentCard(self):
        ''' Returns the current card in play for this game '''
        return self._currentCard
    
    def isFinished(self):
        ''' Returns True if the game is finished, that is if one player has 0 cards '''
        for player in self._playerList:
            if len(player.getCurrentHand()) == 0:
                return True
        return False
    
    def testMove(self, card):
        ''' Test to see if the Card card is a valid move given the current card in play '''
        if not self.currentPlayer().testMove(self._currentCard, card):
                raise InvalidMoveException
        
    def hasUno(self, player):
        ''' Returns True if the Player player has UNO, that is has only one card left '''
        return len(player.getCurrentHand()) == 1

    def nextPlayerHasUno(self):
        ''' Returns true if the next player has UNO (to help the AI) '''
        try:
            return len(self._playerList[self._currentPlayer-1].getCurrentHand) == 1
        except:
            return len(self._playerList[0].getCurrentHand()) == 1
        
    def applySpecial(self,card, color=None):
        ''' Applies the special ability of Card card. '''
        ability = card.getData()
        if ability == 'skip':
            self._currentPlayer+=1
            if self._currentPlayer >= len(self._playerList):
                self._currentPlayer = 0
            return True
        elif ability == 'reverse':

#            if len(self._playerList) > 2: 
#                self._playerList = self._playerList[::-1] #reverse the list
#                self._currentPlayer = abs(self._currentPlayer-len(self._playerList)) #fix order
#                return True
#            return False
            self._playerList = self._playerList[::-1] #reverse the list
            if len(self._playerList) > 2: 
                self._currentPlayer = abs(self._currentPlayer-len(self._playerList)) #fix order
            if self._currentPlayer > len(self._playerList)-1:
                self._currentPlayer=0
            return False
        elif ability == 'draw 2':
            try:
                self._playerList[self._currentPlayer+1].drawCard(2)
                self._currentPlayer+=1
            except:
                self._playerList[0].drawCard(2)
                self._currentPlayer = 0
            return True
        elif ability == 'wild' or ability == 'wild draw four':
            self._currentCard = self._blankCards[color]
            if ability == "wild draw four":
                try:
                    self._playerList[self._currentPlayer+1].drawCard(4)
                    self._currentPlayer+=1
                except:
                    self._playerList[0].drawCard(4)
                    self._currentPlayer=0
            return True


    def doMove(self, player, card, color=None):
        ''' 
        Let the Player player play the Card card.
        First, test if the move is valid. Then apply any special abilities the card may have.
        After that, remove the card from the player's Hand.
        Finally, update the currentPlayer variable
        '''
        self.testMove(card)
        nextPlayer = True
        if card.isSpecial(): nextPlayer = self.applySpecial(card, color)
        player.removeFromHand(card)
        if not card.isWild(): self._currentCard = card
        if nextPlayer:
            self._currentPlayer += 1
            if self._currentPlayer >= len(self._playerList):
                self._currentPlayer=0        
        
    def currentPlayer(self):
        ''' Returns the Player whose turn it is '''
        return self._playerList[self._currentPlayer] 
    
    def getNextPlayerName(self):
        ''' Return the name of the player whose turn it is next '''
        try:
            return self._playerList[self._currentPlayer-1].getName()
        except IndexError:
            return self._playerList[self._currentPlayer].getName()
        
    def playerPasses(self):
        ''' Update the currentPlayer variable when a Player passes '''
        self._currentPlayer += 1
        if self._currentPlayer >= len(self._playerList):
            self._currentPlayer = 0
