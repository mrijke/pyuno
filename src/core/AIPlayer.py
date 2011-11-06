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
    
    def determineColor(self):
        '''
        Returns the desired color to change to after a wild card.
        Does this by determining which color is the most frequent in Hand
        '''
        freq = {'blue':0,'yellow':0,'red':0,'green':0}
        for card in self.getCurrentHand():
            if not card.getColor() == 'blank':
                freq[card.getColor()]+=1
        return max(freq, key=freq.__getitem__)

    def determineMove(self, current, nextplayerhasuno):
        ''' 
        Determine the "best" move to play. 
        Raises a NoMoveFoundException when no valid move can be determined.
        '''
        cards = self.getPlayableCards(current)
        samecolor = []
        samecolor_special = []
        othercolor = []
        othercolor_special = []
        wild = []
        wilddrawfour = []
        for card in cards:
            if card.getColor() == current.getColor(): 
                samecolor.append(card)
                if card.isSpecial(): samecolor_special.append(card)
            elif card.getData() == current.getData():
                othercolor.append(card)
                if card.isSpecial(): othercolor_special.append(card)
            elif card.getData() == "wild":
                wild.append(card)
            elif card.getData() == "wild draw four":
                wilddrawfour.append(card)
        if nextplayerhasuno: #prioritize Wild* cards if next player has uno
            if len(wilddrawfour) > 0:
                return wilddrawfour[0] #choose draw four over normal
            if len(wild) > 0:
                return wild[0]
        if len(samecolor_special) > 0:
            return samecolor_special[0]
        if len(samecolor) > 0:
            return samecolor[0]
        if len(othercolor_special) > 0:
            return othercolor_special[0]
        if len(othercolor) > 0:
            return othercolor[0]
        #if AI gets here no card can be played, so change the color with
        #a wild or wild draw four. After returning this card the Client must
        #ask the AI with the determineColor method which color it wants
        if len(wilddrawfour) > 0: #wild draw four has priority
            return wilddrawfour[0]
        if len(wild) > 0:
            return wild[0]
        raise NoMoveFoundException
