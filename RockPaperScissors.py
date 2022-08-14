import random

comp_score = 0
player_score = 0

def main():
    global comp_score
    global player_score
    player=int(input("Enter a choice (Rock[1], Paper[2], Scissors[3]): "))
    print()
    options=[1,2,3]
    computer=random.choice(options)

    if player==computer:
        print("The computer chose the same thing as well!")
        print("It's a tie!")
    else:
        if player==1:
            if computer==2:
                comp_score+=1
                print("The computer chose Paper!")
                print("Paper beats Rock! The computer won!")
            else:
                player_score+=1
                print("The computer chose Scissors!")
                print("Rock beats Scissors! You won!")
        elif player==2:
            if computer==3:
                comp_score += 1
                print("The computer chose Scissors!")
                print("Scissors beats Paper! The computer won!")
            else:
                player_score += 1
                print("The computer chose Rock!")
                print("Paper beats Rock! You won!")
        elif player==3:
            if computer==1:
                comp_score += 1
                print("The computer chose Rock!")
                print("Rock beats Scissors! The computer won!")
            else:
                player_score += 1
                print("The computer chose Paper!")
                print("Scissors beat Paper! You won!")

while True:
    ch=input("Do you want to play (Y/N): ")
    print()
    if ch.lower()=="y":
        main()
    elif ch.lower()=="n":
        print("You scored", player_score,"points!")
        print("The bot scored", comp_score, "points!")
        break
    else:
        print("Enter a valid choice!")
