import random  # Import the random module to generate random choices for the computer

def get_computer_choice():
    """Function to randomly select the computer's choice."""
    choices = ['rock', 'paper', 'scissors']  # List of possible choices
    return random.choice(choices)  # Return a random choice from the list

def get_user_choice():
    """Function to get the user's choice."""
    user_input = input("Enter your choice (rock, paper, scissors): ").lower()  # Get user input and convert it to lowercase
    # Validate the user's choice
    while user_input not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please try again.")  # Inform the user of the invalid choice
        user_input = input("Enter your choice (rock, paper, scissors): ").lower()  # Prompt for input again
    return user_input  # Return the valid user choice

def determine_winner(user_choice, computer_choice):
    """Function to determine the winner of the game."""
    if user_choice == computer_choice:  # Check if both choices are the same
        return "It's a tie!"  # Return a tie message
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"  # User wins
    else:
        return "You lose!"  # Computer wins

def play_game():
    """Function to play a single round of Rock, Paper, Scissors."""
    print("Welcome to Rock, Paper, Scissors!")  # Welcome message
    user_choice = get_user_choice()  # Get the user's choice
    computer_choice = get_computer_choice()  # Get the computer's choice
    print(f"You chose: {user_choice}")  # Display user's choice
    print(f"Computer chose: {computer_choice}")  # Display computer's choice
    result = determine_winner(user_choice, computer_choice)  # Determine the winner
    print(result)  # Print the result

# Main block to execute the game
if __name__ == "__main__":
    play_game()  # Call the play_game function to start the game