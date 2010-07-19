'''
Created on Jul 19, 2010

@author: rupert
'''

class Player(object):
    '''
    Represents a player in the UNO game.
    Can be human, or can be controlled by an AI.
    '''


    def __init__(self, name, AI=None):
        '''
        Constructs a new Player
        '''
        self._name = name
        self._AI = AI
        self._hand = Hand()
        
        