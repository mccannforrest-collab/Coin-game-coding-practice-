#Coin toss- flip coin x times. Record each flip heads or tails and tally total.


import random


heads = 0
tails = 0

gRun = "y"
while gRun == "y":
    x = int(input("How many times would you like to coin toss: "))
    for i in range(x):
        toss = random.randint(1,2)
        if toss == 1:
                    heads += 1
                    print("Heads")
        elif toss == 2:
                    tails += 1
                    print("Tails")
        else:
                    print("Failed")
    print("Heads total: ", heads)
    print("Tails total: ", tails)
    heads = 0
    tails = 0
    gRun = input("Would you like to play again (y, n)? ")
    if gRun == "n":
             print("Thank you for playing the game.")
    elif gRun!= "y" and "n":
            print("Invalid entry")
    

