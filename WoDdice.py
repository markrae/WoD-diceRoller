import random
##return value can be a dramatic failure, failure, n successes, exceptional success
##dramatic failure will return -1. failure will return 0. n successes will return a positive integer.
def roll(dicepool):
    if dicepool >= 0:
        ##main roll
        outcome = range(dicepool)
        for n in outcome:
            outcome[n] = random.randint(1,10)
        print outcome
        
        ##reroll 10's
        numrerolled = 0
        for n in outcome:
            if n == 10:
                numrerolled += 1
        while numrerolled > 0:
            newdie = random.randint(1,10)
            if newdie != 10:
                numrerolled -= 1
            outcome += [newdie]
            print outcome

        ##count successes
        successes = 0
        if dicepool == 0:
            ##chance die. success only on 10. 10-again?
            outcome = [random.randint(1,10)]
            for n in outcome:
                if n == 10:
                    sucesses +=1
                if n == 1:
                    sucesses = -1
        elif dicepool >= 1:
            ##normal 10-again roll. 8, 9 and 10 are sucesses
            for n in outcome:
                if n == 10:
                    successes += 1
                if n == 9:
                    successes += 1
                if n == 8:
                    successes += 1
        return successes

##def instantAction(dicepool)
##def extendedAction(dicepool)
##def roteAction(dicepool)
        
    
