import random
import string

def generate_password():
    print("--- Quick Password Generator ---")
    length = int(input("Enter password length (e.g., 12): "))
    
    # Combine lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly pick characters based on the length
    password = "".join(random.choice(characters) for i in range(length))
    
    print(f"Your secure password is: {password}")

generate_password()