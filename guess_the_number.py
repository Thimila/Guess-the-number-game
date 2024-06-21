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

# HTML template with CSS and JavaScript for animation
template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>Guess the Number Game</title>
    <style>
      body {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        background-color: #f0f8ff;
        font-family: Arial, sans-serif;
        margin: 0;
      }
      .container {
        text-align: center;
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        animation: fadeIn 2s;
      }
      @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
      }
      h1 {
        color: #333;
      }
      p {
        font-size: 18px;
      }
      form {
        margin-top: 20px;
      }
      input[type="text"] {
        padding: 10px;
        font-size: 16px;
        border-radius: 5px;
        border: 1px solid #ccc;
        width: 200px;
        transition: all 0.3s;
      }
      input[type="text"]:focus {
        border-color: #007bff;
        box-shadow: 0 0 5px rgba(0, 123, 255, 0.5);
      }
      button {
        padding: 10px 20px;
        font-size: 16px;
        color: white;
        background-color: #007bff;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        transition: all 0.3s;
      }
      button:hover {
        background-color: #0056b3;
      }
      .message {
        margin-top: 20px;
        font-size: 20px;
        animation: slideIn 1s;
      }
      @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Guess the Number Game</h1>
      <p>{{ message }}</p>
      <form method="POST">
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
