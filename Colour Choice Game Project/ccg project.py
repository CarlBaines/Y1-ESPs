import random
import time

global userchoice
global computerscore
global playerscore

def gamemenu():
    print("Red = 1 \nYellow = 2 \nOrange = 3\nGreen = 4\nBlue = 5")
    userchoice = int(input("Please enter a number "))
    if userchoice == 1:
        colourchoice = 'red'
    elif userchoice == 2:
        colourchoice = 'yellow'
    elif userchoice == 3:
        colourchoice = 'orange'
    elif userchoice == 4:
        colourchoice = 'green'
    elif userchoice == 5:
        colourchoice = 'blue'
    print("Your choice is " + str.upper(colourchoice))
    print("\nThe computer is now choosing a colour... ")
    return colourchoice, userchoice

def co_choice():
    global userchoice
    global computercolour
    computerchoice = random.randint(1,5)
    if computerchoice == 1:
        computercolour = 'red'
    elif computerchoice == 2:
        computercolour = 'yellow'
    elif computerchoice == 3:
        computercolour = 'orange'
    elif computerchoice == 4:
        computercolour = 'green'
    else:
        computercolour = 'blue'
    print("The computer chose " + str.upper(computercolour))
    return computercolour

def scoring(colourchoice, computercolour):
    global computerscore
    global playerscore
    if colourchoice == computercolour:
        time.sleep(1)
        print("Your guess was CORRECT, you got 1 point!")
        playerscore = playerscore + 1
        time.sleep(1)
        print("Player score: " + str(playerscore))
        time.sleep(1)
        print("Computer score: " + str(computerscore))
        if playerscore > computerscore:
            time.sleep(1)
            print("You have beaten the computer!")
    else:
        time.sleep(1)
        print("Your guess was INCORRECT, you got 1 point!")
        computerscore = computerscore + 1
        time.sleep(1)
        print("Player score: " + str(playerscore))
        time.sleep(1)
        print("Computer score: " + str(computerscore))
        time.sleep(1)
        print("The computer has beaten you!")
        

def secondround(colourchoice, computercolour):
    playagain = input("Do you want to play again? (y/n) ")
    if playagain == 'n' or playagain == 'no':
        quit()
    else:
        play()

def play():
    global computerscore
    global playerscore
    computerscore = 0
    playerscore = 0
    
    colourchoice, userchoice = gamemenu()
    
    computercolour = co_choice()
    scoring(colourchoice, computercolour)
    secondround(colourchoice, computercolour)
play()


        
        
