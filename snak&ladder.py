#snake and ladder
import random
currentposition=0
snake=[32,36,48,62,88,95,97]
ladder=[1,4,8,21,28,50,71,80]

tcount=0
n=int(input("How many players are in the game?"))
if(n==1):
    print("welcome to play Snake and Ladder")
    while(currentposition<100):
        #if(currentposition==100_
        throw=random.randrange(1,7)
        print("value from dice is:",throw)
        tcount=throw
        while(throw==6):
            print("you have one more chance to throw dice")
            throw=random.randrange(1,7)
            tcount+=throw
            print("value from throw:",throw)
            if(throw==6):
                continue
            else:
                throw=tcount
                break
        nextposition=currentposition+throw
        if(nextposition>100):
            print("you need lesser value to win!")
            input("press enter")
            continue
        else:
            print("after throwing a die the position changed from {0} to {1}".format(currentposition, nextposition))
            if nextposition in snake:
                if (nextposition==32):
                    nextposition=10
                elif (nextposition==36):
                    nextposition=6
                elif (nextposition==48):
                    nextposition=26
                elif (nextposition==62):
                    nextposition=18
                elif (nextposition==88):
                    nextposition=24
                elif (nextposition==95):
                    nextposition=56
                elif (nextposition==97):
                    nextposition=78
                print("player got bitten by a snake and now on {0}".format(nextposition))
                currentposition=nextposition
                
            elif nextposition in ladder:
                if (nextposition==1):
                    nextposition=38
                elif (nextposition==4):
                    nextposition=14
                elif (nextposition==8):
                    nextposition=30 
                elif (nextposition==21):
                    nextposition=42
                elif (nextposition==28):
                    nextposition=76
                elif (nextposition==50):
                    nextposition=67
                elif (nextposition==71):
                    nextposition=92
                elif (nextposition==80):
                    nextposition=99
                print("player climbed a ladder and is now on {0}".format(nextposition))
                currentposition=nextposition
            
            else:
                currentposition=nextposition
                print("current position:",currentposition)
            input("press enter")
            continue
    else:
        if(currentposition==100):
            print("congratulations! you won!")
            print("game over")
else:
    print("enter proper input")
    

        
    
