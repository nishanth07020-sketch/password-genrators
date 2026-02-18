import random

# Initialize scores
user_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

print("Welcome to Rock-Paper-Scissors Game!")

while True:
    # User Input
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please try again.")
        continue

    # Computer Selection
    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    # Game Logic
    if user_choice == computer_choice:
        print("It's a tie!")

    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    # Display Scores
    print("Score -> You:", user_score, "| Computer:", computer_score)

    # Play Again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("\nFinal Score -> You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing!")
        break
