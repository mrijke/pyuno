'''
Created on Jul 19, 2010

@author: rupert
'''
import sys
from core.Game import Game, InvalidMoveException
from core.AIPlayer import AIPlayer, NoMoveFoundException

def start():
    print "Welcome to the superawesome pyUNO gaem."
    g = Game()
    g.addPlayerToGame("Sjaak")
    g.addAIPlayerToGame("Kees")
    while not g.isFinished():
        current = g.currentPlayer()
        cards = current.getCurrentHand()
        print "%s turn." % current.getName()
        if not isinstance(current, AIPlayer):
            for card in cards:
                print '%s |' % card,
            print
            print 'Current card: ' + str(g.getCurrentCard())
        notDone = True
        drew = False
        if not isinstance(current, AIPlayer): 
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
                            print '%s draws two cards and skips his turn.' % g.getNextPlayerName()
                        elif selectedcard.getData() == "skip":
                            print "%s skips a turn" % g.getNextPlayerName()
                        elif selectedcard.getData() == "reverse":
                            print "Play order is reversed."
                    if g.hasUno(current):
                        print "%s has UNO! Beware!" % current.getName()
                    notDone = False
        else: #AI Player
            try:
                card = current.determineMove(g.getCurrentCard())
            except NoMoveFoundException:
                current.drawCard()
                try:
                    card = current.determineMove(g.getCurrentCard())
                except NoMoveFoundException:
                    g.playerPasses()
            g.doMove(current, card)
            print "AI player %s played %s" % (current.getName(), str(card))
                    
    print "%s has won this game of UNO! :)" % current.getName()
                