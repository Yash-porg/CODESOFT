import random

def display_instructions():
    print("=" * 40)
    print(" Welcome to Rock-Paper-Scissors! rock")
    print("=" * 40)
    print("Instructions:")
    print("- Choose one: Rock, Paper, or Scissors")
    print("- Rock beats Scissors")
    print("- Scissors beat Paper")
    print("- Paper beats Rock")
    print("- Type 'exit' anytime to quit the game")
    print("=" * 40)

def get_user_choice():
    choice = input(" Enter your choice (rock/paper/scissors): ").lower()
    while choice not in ['rock', 'paper', 'scissors', 'exit']:
        choice = input(" Invalid choice. Please enter rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return " You win!"
    else:
        return " You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    display_instructions()

    while True:
        user_choice = get_user_choice()
        if user_choice == 'exit':
            print("\n Thanks for playing!")
            print(f"Final Score - You: {user_score}, Computer: {computer_score}")
            break

        computer_choice = get_computer_choice()

        print(f"\n You chose: {user_choice.capitalize()}")
        print(f" Computer chose: {computer_choice.capitalize()}")

        result = determine_winner(user_choice, computer_choice)
        print(f" Result: {result}")

        if "win" in result:
            user_score += 1
        elif "lose" in result:
            computer_score += 1

        print(f" Score => You: {user_score} | Computer: {computer_score}\n")
        print("-" * 40)

if __name__ == "__main__":
    play_game()

    
            
