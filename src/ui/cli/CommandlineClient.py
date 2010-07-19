'''
Created on Jul 19, 2010

@author: rupert
'''
from core.Game import Game

def start():
    print "Welcome to the superawesome pyUNO gaem."
    g = Game()
    g.addPlayerToGame("Sjaak", None)
    g.addPlayerToGame("Kees", None)
    while not g.isFinished():
        current = g.nextPlayer()
        cards = current.getCurrentHand()
        print "%s turn. Your hand:" % current.getName()
        for card in cards:
            print '%s |' % card,
        print
        print 'Current card: ' + str(g.getCurrentCard())
        notDone = True
        drew = False
        while notDone:
            selectedcard = int(raw_input("Pick a card number, or 0 to draw a new card/pass. > "))
            if selectedcard == 0 and not drew:
                current.drawCard()
                print "%s draws a card." % current.getName()
                print 'Your hand:'
                for card in cards:
                    print '%s |' % card,
                print
                print 'Current card: ' + str(g.getCurrentCard())
                drew = True
                continue
            if selectedcard == 0 and drew:
                print "%s passes." % current.getName()
                notDone = False
                break
                
            if selectedcard <= len(cards):
                if g.doMove(current, cards[selectedcard-1]):
                    notDone = False
                    break
                print "Not a valid move."