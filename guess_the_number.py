import random

# Define the range for the random number
lower_bound = 1
upper_bound = 100

# Generate a random number
target_number = random.randint(lower_bound, upper_bound)

# Initialize the number of attempts
attempts = 0

# Maximum number of attempts
max_attempts = 10

print(f"Welcome to the Guess the Number game!")
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess what it is?")

while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")

    # Check if the input is a valid number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < target_number:
        print("Too low! Try again.")
    elif guess > target_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number in {attempts} attempts.")
        break
else:
    print(f"Sorry, you've used all {max_attempts} attempts. The number was {target_number}.")
