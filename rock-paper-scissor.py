
import random

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

def rock_paper_scissors():
    choices = ['rock', 'paper', 'scissors']
    while True:
        print("\nRock, Paper, Scissors!")
        player_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
        if player_choice == 'q':
            print("Exiting game. Goodbye!")
            break
        elif player_choice not in choices:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(choices)
        print("Computer chooses:", computer_choice)
        
        winner = determine_winner(player_choice, computer_choice)
        print(winner)

if __name__ == "__main__":
    rock_paper_scissors()
