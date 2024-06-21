from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# Define the range for the random number
lower_bound = 1
upper_bound = 100

# Generate a random number
target_number = random.randint(lower_bound, upper_bound)

# Initialize the number of attempts
attempts = 0

# Maximum number of attempts
max_attempts = 10

# HTML template
template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Guess the Number Game</title>
  </head>
  <body>
    <div>
      <h1>Guess the Number Game</h1>
      <p>{{ message }}</p>
      <form method="POST">
        <label for="guess">Enter your guess:</label>
        <input type="text" id="guess" name="guess" required>
        <button type="submit">Submit</button>
      </form>
      <p>Attempts: {{ attempts }} / {{ max_attempts }}</p>
    </div>
  </body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def game():
    global target_number, attempts
    message = f"I'm thinking of a number between {lower_bound} and {upper_bound}. Can you guess what it is?"

    if request.method == 'POST':
        guess = request.form['guess']
        
        # Check if the input is a valid number
        if not guess.isdigit():
            message = "Please enter a valid number."
        else:
            guess = int(guess)
            attempts += 1

            if guess < target_number:
                message = "Too low! Try again."
            elif guess > target_number:
                message = "Too high! Try again."
            else:
                message = f"Congratulations! You've guessed the number in {attempts} attempts."
                attempts = 0
                target_number = random.randint(lower_bound, upper_bound)  # Reset the game

        if attempts >= max_attempts:
            message = f"Sorry, you've used all {max_attempts} attempts. The number was {target_number}. Let's start a new game."
            attempts = 0
            target_number = random.randint(lower_bound, upper_bound)  # Reset the game

    return render_template_string(template, message=message, attempts=attempts, max_attempts=max_attempts)

if __name__ == '__main__':
    app.run(debug=True)
