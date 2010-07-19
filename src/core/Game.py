'''
Created on Apr 23, 2010

@author: rupert
'''
from Deck import Deck

class Game(object):
    '''
    This represents a game of UNO. It keeps track of a list of the players currently involved in the game.
    '''

    def __init__(self):
        '''
        
        '''
        self._player_list = []
        self._deck = Deck()
        self._deck.shuffle()
        self._game_finished = False
    
    def getDeck(self):
        return self._deck
    
    def addPlayerToGame(self, player):
        self._player_list.append(player)
    
    def startGame(self):
        currentCard = self._deck.drawCard()
        while not self._game_finished:
            for player in self._player_list:
                move = player.askMove(currentCard)
                
        