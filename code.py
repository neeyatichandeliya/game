from random import randint

#create list
t = ["Rock", "Paper", "Scissors"]

#assign a random play to the opponent
opponent = t[randint(0,2)]

#set p to False
p = False

while p == False:
#set p to True
    p = input("Rock, Paper, Scissors?")
    if p == opponent:
        print("Tie!")
    elif p == "Rock":
        if opponent == "Paper":
            print("You lose!", opponent , "covers", p)
        else:
            print("You win!", p, "smashes", opponent )
    elif p == "Paper":
        if opponent == "Scissors":
            print("You lose!", opponent , "cut", p)
        else:
            print("You win!", p, "covers", opponent )
    elif p == "Scissors":
        if opponent  == "Rock":
            print("You lose...", opponent , "smashes", p)
        else:
            print("You win!", p, "cut", opponent )
    else:
        print("That's not a valid play. Check your spelling!")
    #p was set to True, but we want it to be False so the loop continues
    p = False
    opponent  = t[randint(0,2)]
