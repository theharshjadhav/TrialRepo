import random


user_wins = 0
computer_wins = 0
options = ['rock','paper','scissors']

print("ROCK PAPER SCISSORS GAME")

while True:
    user_input = input("Enter your Choice Rock/Paper/Scissors or press Q to quit\n").lower()
    if user_input == 'q':
        break
    if user_input not in ["rock", "paper", "scissors"]:
        print("Enter a valid choice! ")
        continue
    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print(f"USER:{user_input}")
    print(f"COMPUTER:{computer_pick}")


    if user_input == computer_pick:
        print("It's a Draw! ")

    elif user_input == "rock" and computer_pick == "paper":
        print("You lose! ")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "scissor":
        print("You Lose!")
        user_wins += 1

    elif user_input == "scissor" and computer_pick == "rock":
        print("You Lose!")
        user_wins += 1
    else:
        print("You won")
        computer_wins += 1



print(f"The total score for User is {user_wins}")
print(f"The total score for Computer is {computer_wins}")

if computer_wins > user_wins:
    print("You Lost!")
else:
    print("You won!")