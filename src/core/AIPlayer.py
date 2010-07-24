'''
Created on Jul 24, 2010

@author: rupert
'''
from Player import Player

class NoMoveFoundException(Exception):
    pass

class AIPlayer(Player):
    '''
    classdocs
    '''
    def __init__(self, name, deck):
        '''
        Constructor
        '''
        Player.__init__(self, name, deck)
        
    def determineMove(self, current):
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