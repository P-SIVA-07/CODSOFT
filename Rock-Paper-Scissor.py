import random as randint
t=("Rock","Scissor","Paper")
computer=randint.choice(t)
player=False
while player==False:
    player=input("Rock,Paper,Scissor?:")
    if player==computer:
        print("Tie!")
    elif player=="Rock":
        if computer=="Pape":
            print("you loose")
        else:
            print("you win!")

    elif player=="Scissor":
        if computer=="Rock":
            print("you loose")
        else:
            print("you win!")
    elif player=="Paper":
        if computer=="Scissor":
            print("you loose")
        else:
            print("you win")
    else:
        print("invalid spell reenter!")
player==False
computer=randint.choice(t)
