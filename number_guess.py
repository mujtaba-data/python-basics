import random

# Let's start the game!
print("Welcome to the Number Guess Game!")

# Picking a random number for the player to guess
secret_number = random.randint(1, 50)  # changed variable name to something more descriptive
num_attempts = 0  # keeping track of how many tries

while True:
    # Get the user's guess
    user_guess = int(input("Guess a number between 1 and 50: "))
    num_attempts = num_attempts + 1  # could use += but being explicit here
    
    # Check if guess is correct
    if user_guess < secret_number:
        print("Too low! Try again.")
    elif user_guess > secret_number:
        print("Too high! Try again.")
    else:
        # They got it right!
        print(f"Congratulations! You guessed the number {secret_number} in {num_attempts} attempts.")
        break  # exit the loop
