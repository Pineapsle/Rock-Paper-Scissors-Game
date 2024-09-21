import random

#Greet user
print("Welcome to Rock, Paper or Scissors! \nCan you beat the computer?")
user = input("\nWhat is your name? ")
print("\nHello " + user.capitalize() + "! Lets play!\n Make choices to beat the computer\n Rock beats Scissors, Paper beats "
                        "rock and Scissors beats Paper\n")

#Global variables
user_wins = 0
computer_wins = 0
total_plays = 0
avg_win_rate = 0
streak = 0
draws = 0
rock = 0
paper = 0
scissors = 0

choices = ["rock", "paper", "scissors"]

while True:
    user_input = input("Rock,Paper,Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in choices:
        continue

    random_num = random.randint(0, 2)
    # The computer picks a random choice of rock, paper or scissors
    computer_choice = choices[random_num]
    print("Computer:", computer_choice + ".")

    if user_input == "rock":
        rock += 1
    if user_input == "paper":
        paper += 1
    if user_input == "scissors":
        scissors += 1

    if user_input == "rock" and computer_choice == "scissors":
        print("You win!\n")
        user_wins += 1
        total_plays += 1
        streak += 1

    elif user_input == "paper" and computer_choice == "rock":
        print("You win!\n")
        user_wins += 1
        total_plays += 1
        streak += 1

    elif user_input == "scissors" and computer_choice == "paper":
        print("You win!\n")
        user_wins += 1
        total_plays += 1
        streak += 1

    elif user_input == computer_choice:
        print("You drew!\n")
        draws += 1
        total_plays += 1
        streak = 0
    else:
        print("You lose!\n")
        computer_wins += 1
        total_plays += 1
        streak = 0

print("\n-----------------------------------------------------------")
print("You won", user_wins, "times.")
print("The computer won", computer_wins, "times.")
print("You drew", draws, "times.")
print("-----------------------------------------------------------")
print("You chose rock", rock, "times.")
print("You chose paper", paper, "times.")
print("You chose scissors", scissors, "times.")
print("-----------------------------------------------------------")
print("You played a total of", total_plays, "times.")
print("You had an average win rate of", (user_wins/total_plays)*100, "%")
print("You had a winning steak of", streak,"wins.")
print("-----------------------------------------------------------")
