import random
choice = ['Rock','Paper','Scissor']
while True:
    print("Welcome !")
    user_count=0
    comp_count=0
    for i in range(1,4):
        print("Round = ",i)
        print("Enter an integer : ")
        print(" 1 for selecting ROCK")
        print(" 2 for selecting PAPER")
        print(" 3 for selecting SCISSOR")
        your_choice=int(input())

        if(your_choice==1):
            print("You have Selected Rock")
            your_choice="Rock"
        elif(your_choice==2):
            print("You have selected Paper")
            your_choice="Paper"
        elif(your_choice==3):
            print("You have selected Scissor")
            your_choice="Scissor"
        else:
            print("You have Entered wrong choice,  Please Select Again ")
            break


        computerChoice= random.choice(choice)
        print("Computer Selects ",computerChoice)

        if(your_choice==computerChoice):
             print("Drawn")
        elif((your_choice=='Paper' and computerChoice=='Rock') or (your_choice=='Rock' and computerChoice=='Scissor') or(your_choice=='Scissor' and computerChoice=='Paper')):
             user_count = user_count + 1
        elif((your_choice=='Rock' and computerChoice=='Paper') or (your_choice=='Scissor' and computerChoice=='Rock') or(your_choice=='Paper' and computerChoice=='Scissor')):
             comp_count = comp_count + 1



    if(user_count>comp_count):
        print("You win! ")
    elif(user_count<comp_count):
        print("Computer wins! ")
    else:
        print("Drawn ")

    print("Do you want to play again? Yes or No ")
    x=input("Enter yes or no    ")
    if(x == 'Yes' or x == 'yes' or x == 'YES'):
        continue
    else:
        break


