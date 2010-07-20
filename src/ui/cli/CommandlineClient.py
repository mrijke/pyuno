'''
Created on Jul 19, 2010

@author: rupert
'''
import sys
from core.Game import Game, InvalidMoveException

def start():
    print "Welcome to the superawesome pyUNO gaem."
    g = Game()
    g.addPlayerToGame("Sjaak", None)
    g.addPlayerToGame("Kees", None)
    while not g.isFinished():
        current = g.currentPlayer()
        cards = current.getCurrentHand()
        print "%s turn. Your hand:" % current.getName()
        for card in cards:
            print '%s |' % card,
        print
        print 'Current card: ' + str(g.getCurrentCard())
        notDone = True
        drew = False
        while notDone:
            try:
                selectedcardnumber = int(raw_input("Pick a card number, or 0 to draw a new card/pass. > "))
            except KeyboardInterrupt:
                sys.exit(1)                
            
            if selectedcardnumber == 0 and not drew:
                current.drawCard()
                print "%s draws a card." % current.getName()
                print 'Your hand:'
                for card in cards:
                    print '%s |' % card,
                print
                print 'Current card: ' + str(g.getCurrentCard())
                drew = True
                continue
            if selectedcardnumber == 0 and drew:
                print "%s passes." % current.getName()
                g.playerPasses()
                notDone = False
                break
        
            if selectedcardnumber <= len(cards):
                try:
                    selectedcard = cards[selectedcardnumber-1]
                    g.doMove(current, selectedcard)
                except InvalidMoveException:
                    print "Not a valid move."
                    continue
                if selectedcard.isSpecial():
                    if selectedcard.getData() == "draw 2":
                        print '%s draws two cards' % g.getNextPlayerName()
                    elif selectedcard.getData() == "skip":
                        print "%s skips a turn" % g.getNextPlayerName()
                    elif selectedcard.getData() == "reverse":
                        print "Play order is reversed."
                if g.hasUno(current):
                    print "%s has UNO! Beware!" % current.getName()
                notDone = False
    print "%s has won this game of UNO! :)" % current.getName()
                