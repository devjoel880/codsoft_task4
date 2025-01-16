import random
import customtkinter as ctk

# Initialize main window
window = ctk.CTk()
window.title("Rock, Paper, Scissors Game")
window.geometry("400x400")

# Initialize scores
user_score = 0
computer_score = 0

# Function to get computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Function to update the display
def update_display(result, user_choice, computer_choice):
    global user_score, computer_score

    # Determine winner
    winner = determine_winner(user_choice, computer_choice)

    # Update scores
    if winner == "user":
        user_score += 1
    elif winner == "computer":
        computer_score += 1

    # Update result labels
    result_label.configure(text=f"Result: {winner.capitalize()}")
    user_choice_label.configure(text=f"You chose: {user_choice}")
    computer_choice_label.configure(text=f"Computer chose: {computer_choice}")
    score_label.configure(text=f"Score: You - {user_score} | Computer - {computer_score}")

# Button click handlers for user choices
def rock_button_clicked():
    computer_choice = get_computer_choice()
    update_display("playing", "rock", computer_choice)

def paper_button_clicked():
    computer_choice = get_computer_choice()
    update_display("playing", "paper", computer_choice)

def scissors_button_clicked():
    computer_choice = get_computer_choice()
    update_display("playing", "scissors", computer_choice)

# Define the UI elements
rock_button = ctk.CTkButton(window, text="Rock", command=rock_button_clicked)
rock_button.pack(pady=10)

paper_button = ctk.CTkButton(window, text="Paper", command=paper_button_clicked)
paper_button.pack(pady=10)

scissors_button = ctk.CTkButton(window, text="Scissors", command=scissors_button_clicked)
scissors_button.pack(pady=10)

# Labels to show the game state
result_label = ctk.CTkLabel(window, text="Result: ", font=("Arial", 14))
result_label.pack(pady=10)

user_choice_label = ctk.CTkLabel(window, text="You chose: ", font=("Arial", 12))
user_choice_label.pack(pady=5)

computer_choice_label = ctk.CTkLabel(window, text="Computer chose: ", font=("Arial", 12))
computer_choice_label.pack(pady=5)

score_label = ctk.CTkLabel(window, text="Score: You - 0 | Computer - 0", font=("Arial", 12))
score_label.pack(pady=10)

# Start the GUI loop
window.mainloop()
