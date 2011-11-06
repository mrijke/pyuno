'''
Created on Apr 15, 2010

@author: rupert
'''
from Card import Card
from random import randint

class EmptyDeckException(Exception):
    pass

class Deck(object):
    '''
    Represents an UNO card deck.
    Consists of four colors: red, blue, yellow and green.
    Every color has two times 1-9 and one zero.
    There are also special cards; each color has them.
    Special cards include Skip, Draw 2, Reverse.
    Each color has one of every special card.
    There are also two non color-specific cards: Wild, and Wild Draw Four.  
    Four of each are included in the deck.
    '''
   
    _card_colors = ['red', 'green', 'yellow', 'blue']
    _special_cards = ['skip', 'draw 2', 'reverse']
    _nocolor_special_cards = ['wild', 'wild draw four']

    def __init__(self):
        '''
        Constructs a deck of cards.
        '''

        self._cards = []
        for color in self._card_colors:
            self._cards.append(Card(color,0)) #add one 0 card per color
            for x in range(2): #2 normal cards of every color
                for i in range(1,10): #creating the normal cards
                    self._cards.append(Card(color,i))
                for prop in self._special_cards:
                    self._cards.append(Card(color, prop))
        for card in self._nocolor_special_cards:
            for x in range(4):
                self._cards.append(Card('blank', card))
                
    def drawCard(self, amount=1):
        ''' Returns (draws) the top card '''
        cards = []
        for x in range(amount):
            try:
                cards.append(self._cards.pop(0))
            except:
                raise EmptyDeckException
        if len(cards) == 1:
            return cards[0]
        else:
            return cards
    
    def draw7Cards(self):
        ''' Return (draw) 7 cards. Used for the initial cards when starting a new game. '''
        res = []
        for x in range(7):
            res.append(self.drawCard())            
        return res
    
    def shuffle(self):
        ''' Shuffle the deck. A list is returned filled with all the cards from the deck randomly picked. '''
        newdeck =[]
        for i in range(0,len(self._cards)):
            x = randint(0,len(self._cards)-1)
            newdeck.append(self._cards[x])
            self._cards.pop(x)
        self._cards = newdeck
        
    def printDeck(self):
        ''' Print the deck using the string representation of the cards '''
        for card in self._cards:
            print card    
    
if __name__ == "__main__":
    dek = Deck()
    print len(dek._cards)
