'''
Created on Jul 24, 2010

@author: rupert
'''
from Player import Player

class NoMoveFoundException(Exception):
    pass

class AIPlayer(Player):
    '''
    This class represents a simple AI opponent.
    The strategy is very basic; the order of cards the opponent plays is:
    *    Same color, action cards
    *    Same color, normal cards
    *    Other color, action cards
    *    Other color, normal card
    When the AI is unable to find a move, a NoMoveFoundException is raised.
    The Client should catch this and draw another card using the Player.drawCard() method.
    Then the determineMove() method can be called again to see if a move is possible.
    When there is again no move possible, the Client should pass.
    '''
    def __init__(self, name, deck):
        ''' Construct an AIPlayer (only calls the super.__init__() '''
        Player.__init__(self, name, deck)
        
    def determineMove(self, current):
        ''' Determine the "best" move to play. 
        Raises a NoMoveFoundException when no valid move can be determined. '''
        cards = self.getPlayableCards(current)
        samecolor = []
        samecolor_special = []
        othercolor = []
        othercolor_special = []
        for card in cards:
            if card.getColor() == current.getColor(): 
                samecolor.append(card)
                if card.isSpecial(): samecolor_special.append(card)
            else:
                othercolor.append(card)
                if card.isSpecial(): othercolor_special.append(card)
        if len(samecolor_special) > 0:
            return samecolor_special[0]
        if len(samecolor) > 0:
            return samecolor[0]
        if len(othercolor_special) > 0:
            return othercolor_special[0]
        if len(othercolor) > 0:
            return othercolor[0]
        raise NoMoveFoundException