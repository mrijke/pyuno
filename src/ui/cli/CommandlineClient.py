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
    humanplayers = int(raw_input("How many human players are playing? "))
    if humanplayers > 0:
        for x in range(humanplayers):
            g.addPlayerToGame(str(raw_input("Name of human player %d? " % (x+1)\
                    )))
    aiplayers = int(raw_input("How many AI Players are playing? "))
    if aiplayers > 0:
        for x in range(aiplayers):
            g.addAIPlayerToGame(str(raw_input("Name of AI Player %d? " % (x+1)\
                    )))
    if aiplayers + humanplayers <= 1:
        print "You cannot start a game with %d player(s)!" % (aiplayers+humanplayers)
        sys.exit(1)
    while not g.isFinished():
        current = g.currentPlayer()
        cards = current.getCurrentHand()
        print "%s turn." % current.getName()
        print 'Current card: ' + str(g.getCurrentCard())
        passed = False
        if not isinstance(current, AIPlayer): 
            print "Your hand: ",
            for card in cards:
                print '%s |' % card,
            print
            notDone = True
            drew = False
            while notDone:
                try:
                    selectedcardnumber = int(raw_input("Pick a card number, or 0 to draw a new card/pass.  "))
                except KeyboardInterrupt:
                    sys.exit(1)                
                
                if selectedcardnumber == 0 and not drew:
                    current.drawCard()
                    print "%s draws a card." % current.getName()
                    print 'Your hand:',
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
                    passed = True
                    break
            
                if selectedcardnumber <= len(cards):
                    try:
                        selectedcard = cards[selectedcardnumber-1]
                        if selectedcard.isWild(): #requires more user input
                            while 1:
                                c = str(raw_input("Choose a color: "))
                                if c in ['blue','yellow','green','red']:
                                    break
                            g.doMove(current, selectedcard, c)
                        else:
                            g.doMove(current, selectedcard)
                    except InvalidMoveException:
                        print "Not a valid move."
                        continue
                    notDone = False
        else: #AI Player
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
                    passed = True
                    continue
            g.doMove(current, selectedcard)
            print "AI player %s played %s" % (current.getName(), str(selectedcard))
        
        if not passed:
            if selectedcard.getData() == "draw 2":
                print '%s draws two cards and skips his turn.' % g.getNextPlayerName()
            elif selectedcard.getData() == "skip":
                print "%s skips a turn" % g.getNextPlayerName()
            elif selectedcard.getData() == "reverse":
                print "Play order is reversed."
            elif selectedcard.getData() == "wild draw four":
                print "%s draws two cards and skips his turn." % g.getNextPlayerName()
            elif selectedcard.getData() == "wild" or selectedcard.getData() == "wild draw four":
                print "The color has been changed to %s" % g.getCurrentCard().getColor()

        if g.hasUno(current):
            print "%s has UNO! Beware!" % current.getName()
                                    
    print "%s has won this game of UNO! :)" % current.getName()
                
