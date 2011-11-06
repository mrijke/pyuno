'''
Created on 06-11-2011
'''

from Deck import Deck

class DiscardPile(Deck):

    def __init__(self):
        self._cards = []

    def addCard(self, card):
        self._cards.append(card)
