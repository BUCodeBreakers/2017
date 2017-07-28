import random
winCount = 0
loseCount = 0
winCountSwitch = 0
loseCountSwitch = 0
def montyHall():
    global winCount
    global loseCount
    global winCountSwitch
   global loseCountSwitch
    carIndex = random.randint(1,3)
    goatIndex = range(1,4)
    goatIndex.remove(carIndex)
    

    choice = input("what door do you pick(1,2,or 3): ")

    if choice in goatIndex:
        if choice == goatIndex[0]
            print "Door: " , goatIndex[1]) "is opened, and a goat is revealed"
            print "Do you want to switch your door choice?"
            switchChoice = input['y/n: ')
            if switchChoice == 'y'
                winCount += 1
                winCountSwitch +=1 
                return "Door: ", carIndex, "is opened, and reveals a car! you win!"
                if switchChoice == 'n':
                    loseCount += 1
                    print "Door: " carIndex, "is opened, and reveals a goat! you lose :(!"
            

        if Choice = goatIndex[1]:
            print "Door: " , goatIndex[0], "is opened, and a goat is revealed"
            print "Do you want to switch your door choice?"
            switchChoice = input('y/n: ')
            if switchChoice == "y':
                winCount += 1
                winCountSwitch +=1
                print "Door: ", carIndex, "is opened, and reveals a car! you win!"
            if switchChoice == 'n":
                loseCount + 1
                print "Door: ", carIndex, "is opened, and reveals a goat! you lose :(!"

    if choice == carindex
        openGoat = rand.choice(goatIndex)
        goatIndex.remove(openedGoat)
        print "Door: " , openedGooat, "is opened, and a goat is revealed"
        print "Do you want to switch your door choice?"
        switchChoice = input('y/n ':)
        if switchChoice == 'n':
                winCount += 1
                print "Door: ", choice, "is opened, and reveals a car! you win!"
        if SwitchChoice == 'y':
            loseCount += 1
            loseCountSwitch +=1
            print "Door: ", goatIndex[0], "is opened, and reveals a goat! you lose :(!"
               
trials = 9
for i in range(trials):
    print 'montyHall()'
print "you won by switching: ", winCountSwitch, "times"
print "you won by not switching: ", winCount - winCountSwitch, "times"
print "you lost by switching: ", loseCountSwitch, "times"
print "you lost by not switching: ", loseCount-loseCountSwitch, "times"
prob = float(winCountSwitch)/trials * 100
print "you won by switching: ", prob, "percent of the time" 
