#!/usr/bin/env python
import sys
import random
##results can be a dramatic failure, failure, n successes, exceptional success
##dramatic failure will return -1. failure will return 0. n successes will return a positive integer.
def roll(dicepool,reRollNumber):
    ## Regular dice roll
    if dicepool > 0:
        ##main roll
        outcome = range(dicepool)
        for n in outcome:
            outcome[n] = random.randint(1,10)
        print outcome

        ##reroll 10's (or 9's or 8's)
        numrerolled = 0
        for n in outcome:
            if n >= reRollNumber:
                numrerolled += 1
        while numrerolled > 0:
            newdie = random.randint(1,10)
            if newdie != 10:
                numrerolled -= 1
            outcome += [newdie]
            print outcome

        ##count successes
        successes = 0
        ##normal 10-again roll. 8, 9 and 10 are sucesses
        for n in outcome:
            if n == 10:
                successes += 1
            if n == 9:
                successes += 1
            if n == 8:
                successes += 1
                
    ## Chance die
    elif dicepool <= 0:
        ##chance die. success only on 10. 10-again
        outcome = [random.randint(1,10)]
        print outcome
        successes = 0
        if outcome == [1]:
            ##dramatic failure only if you roll 1 on your initial chance roll
            successes = -1
        if outcome == [10]:
            ##reroll 10's
            numrerolled = 1
            while numrerolled > 0:
                newdie = random.randint(1,10)
                if newdie != 10:
                    numrerolled -= 1
                outcome += [newdie]
                print outcome
            ##count successes
            successes = 0
            ##only 10's are sucesses, even on rerolls
            for n in outcome:
                if n == 10:
                    successes += 1
        ##else: ##regular failure        
    return successes

if len(sys.argv)>1: ##if there are arguments
    if sys.argv[1].isdigit()==True:
        print roll(int(sys.argv[1]),10)
    elif sys.argv[1]=="-9" and sys.argv[2].isdigit()==True:
        print roll(int(sys.argv[2]),9)
    elif sys.argv[1]=="-8" and sys.argv[2].isdigit()==True:
        print roll(int(sys.argv[2]),8)
    else:
        print "Please only enter numeric arguments at this time."
##def instantAction(dicepool)
##def extendedAction(dicepool)
##def roteAction(dicepool)
