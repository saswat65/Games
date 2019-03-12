import time
import random
print ("Welcome to the Rock, Paper, Scissors Game!")
time.sleep(1)
rounds = int(input("How many rounds would you like to play?"))
print("Challenge accepted! I will play you for", rounds, "rounds! Let's begin!!!")
print("Press r for rock\nPress p for paper\nPress s for scissor")
counter = 0
swagat = rounds
while counter <= rounds-1:
    while rounds not in range(1,1000000):
        try:
            rounds = int(input("Sorry! I can only play between 1 and 1000000 rounds. Try again:"))
        except:
            print ("ERROR invalid input. Out of range or wrong type of data.")
    if rounds in range(1,1000000):
        time.sleep(1)
    options = ("r", "p", "s")
    userChoice = input("Rock, Paper or Scissors?")
    while userChoice not in options:
        try:
            userChoice = input("Not an option friend. Rock, paper or scissors")
        except:
            print ("ERROR invalid input. Wrong type of data.")
    cpuoption1 =  "r"
    cpuoption2 =  "p"
    cpuoption3 =  "s"
    cpuChoice = random.randint(1,3)
    answer = ""
    if cpuChoice == 1:
        answer = cpuoption1
    elif cpuChoice == 2:
        answer = cpuoption2
    elif cpuChoice == 3:
        answer = cpuoption3
    print ("I choose", answer,"")
    user= 0
    cpu = 0
    if userChoice == "r" and answer == cpuoption1:        
        print (" Tie ")
        counter += 1
        swagat -= 1
        print("Remaining rounds", swagat )
    elif userChoice == "p" and answer == cpuoption2:
        print("Tie")
        counter += 1
        swagat -= 1
        print("Remaining rounds",  swagat)
    elif userChoice == "s" and answer == cpuoption3:
        print ("Tie")
        counter += 1
        swagat -= 1
        print("Remaining rounds", swagat)
    elif userChoice == "r" and answer == cpuoption2:
        cpu+=1
        print ("CPU wins the round!")
        counter += 1
        swagat -= 1
        print("Remaining rounds", swagat)
    elif userChoice == "r" and answer == cpuoption3:
        user+=1
        print ("Player wins the round!")
        counter += 1
        swagat -= 1
        print("Remaining rounds", swagat)
    elif userChoice == "p" and answer == cpuoption1:
        user+=1
        print ("Player wins the round!")
        counter += 1
        swagat -= 1
        print("Remaining rounds", swagat)
    elif userChoice == "p" and answer == cpuoption3:
        cpu+=1
        print ("CPU wins the round!")
        counter += 1
        swagat -= 1
        print("Remaining rounds", swagat)
    elif userChoice == "s" and answer == cpuoption1:
        cpu+=1
        print ("CPU wins the round!")
        counter += 1
        swagat -= 1
        print("Remaining rounds", swagat)
    elif userChoice == "s" and answer == cpuoption2:
        user+=1
        print ("Player wins the round!")
        counter += 1
        swagat -= 1
        print("Remaining rounds", swagat)
print(cpu, user)
if cpu > user:
    print("CPU beat the player!")
elif user > cpu:
    print("Player beat the CPU!")
    counter += 1
else :
    print("Looks like that was a Good game, That ended in a tie")
    counter += 1
        