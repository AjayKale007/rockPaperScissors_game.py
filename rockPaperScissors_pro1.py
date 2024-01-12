import random
userChoice=int(input("Enter your choice: type 0 for rock , 1 for paper, 2 for scissors: "))
computerChoice=random.randint(0,2)

print("computer choice:")
print(computerChoice)
if userChoice >= 3 or userChoice <0:
    print("Please enter a valid number!. You Loose.")
else:
    if computerChoice == userChoice:
        print("It`s a draw.")

    elif computerChoice == 0 and userChoice == 2:
        print("You loose.")
    elif userChoice == 0 and computerChoice == 2:
        print("Congradulation ! You win the game.")
    elif computerChoice > userChoice:
        print("You Loose.")
    elif computerChoice < userChoice:
        print("Congradulation ! You win the game.")

