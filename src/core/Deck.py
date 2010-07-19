'''
Created on Apr 15, 2010

@author: rupert
'''
from Card import Card
from random import randint

class Deck(object):
    '''
    Represents an UNO card deck.
    Consists of four colors: red, blue, yellow and green.
    Every color has two times 1-9 and one zero.
    There are also special cards; each color has them.
    Special cards include Skip, Draw 2, Reverse.
    Each color has one of every special card.
    There are also two non color-specific cards: Wild, and Wild Draw Four.  
    '''
   
    def __init__(self):
        '''
        Constructs a deck of cards.
        '''
        self._card_colors = ['red', 'green', 'yellow', 'blue']
        self._special_cards = ['skip', 'draw', 'reverse']

        self._cards = []
        for color in self._card_colors:
            for x in range(1): #2 normal cards of every color
                for i in range(1,10): #creating the normal cards
                    self._cards.append(Card(color,i))
            for prop in ['skip', 'draw2','reverse']:
                self._cards.append(Card(color, prop))
                
    def drawCard(self):
        ''' Draws the top card '''
        return self._cards.pop(0)
        
    def shuffle(self):
        newdeck =[]
        for i in range(0,len(self._cards)):
            x = randint(0,len(self._cards)-1)
            newdeck.append(self._cards[x])
            self._cards.pop(x)
        self._cards = newdeck
        
    def printDeck(self):
        for card in self._cards:
            print card    
    
if __name__ == "__main__":
    dek = Deck()
    dek.printDeck()
    print '-'*50
    dek.shuffle()
    dek.printDeck()