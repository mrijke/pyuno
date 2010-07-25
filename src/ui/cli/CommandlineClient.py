'''
Created on Jul 19, 2010

@author: rupert
'''
import sys, time
from core.Game import Game, InvalidMoveException
from core.AIPlayer import AIPlayer, NoMoveFoundException

def start():
    print "Welcome to the superawesome pyUNO gaem."
    g = Game()
    g.addAIPlayerToGame("Sjaak")
    g.addAIPlayerToGame("Kees")
    g.addAIPlayerToGame("Rupert")
    g.addAIPlayerToGame("Ruben1")
    g.addAIPlayerToGame("Ruben2")
    g.addAIPlayerToGame("Ruben3")
    while not g.isFinished():
        current = g.currentPlayer()
        cards = current.getCurrentHand()
        print "%s turn." % current.getName()
        if not isinstance(current, AIPlayer):
            for card in cards:
                print '%s |' % card,
            print
            print 'Current card: ' + str(g.getCurrentCard())
        if not isinstance(current, AIPlayer): 
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
                    notDone = False
        else: #AI Player
            print "Current card %s" % g.getCurrentCard()
            print "AI player %s is thinking..." % current.getName()
            time.sleep(1)
            try:
                selectedcard = current.determineMove(g.getCurrentCard())
            except NoMoveFoundException:
                print "AI draws a card."
                current.drawCard()
                try:
                    selectedcard = current.determineMove(g.getCurrentCard())
                except NoMoveFoundException:
                    print "AI passes"
                    g.playerPasses()
                    continue
            g.doMove(current, selectedcard)
            print "AI player %s played %s" % (current.getName(), str(selectedcard))
        
        if selectedcard.isSpecial():
            if selectedcard.getData() == "draw 2":
                print '%s draws two cards and skips his turn.' % g.getNextPlayerName()
            elif selectedcard.getData() == "skip":
                print "%s skips a turn" % g.getNextPlayerName()
            elif selectedcard.getData() == "reverse":
                print "Play order is reversed."
        if g.hasUno(current):
            print "%s has UNO! Beware!" % current.getName()
                                    
    print "%s has won this game of UNO! :)" % current.getName()
                