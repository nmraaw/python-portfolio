import random

def play_rps():
    choices = ["rock", "paper", "scissors"]
    print("--- Rock, Paper, Scissors ---")
    
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Please look at your spelling.")
        return
        
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    
    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You win!")
    else:
        print("😢 Computer wins!")

play_rps()