import random

def get_user_choice():
    choice = input("Enter Rock, Paper, or Scissors: ").strip().lower()
    if choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Try again.")
        return get_user_choice()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'paper' and computer == 'rock') or \
         (user == 'scissors' and computer == 'paper'):
        return "user"
    else:
        return "computer"

def play_game():
    user_points = 0
    computer_points = 0

    while True:
        try:
            total_rounds = int(input("Enter the number of rounds you want to play: "))
            if total_rounds < 1:
                print("Please enter a number greater than 0.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


    for round_number in range(1, total_rounds + 1):
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win this round!")
            user_points += 1
        else:
            print("Computer wins this round!")
            computer_points += 1

        print(f"Score: You {user_points} - Computer {computer_points}")

    print(f"\nFinal Score: You {user_points} - Computer {computer_points}")
    if user_points > computer_points:
        print("Congratulations! You won the game!")
    elif user_points < computer_points:
        print("Computer won the game. Better luck next time!")
    else:
        print("The game ended in a tie!")
    print("Thanks for playing Rock, Paper, Scissors with points!")

# Start the game
play_game()