# EDX's Terminal Number Game
## Welcome to EDX'S Terminal Number Game! This simple Python script allows users to play a number guessing game right from their terminal. With just a few lines of code, you can enjoy a fun and interactive experience.

# How to Play
Clone or download the Python script main.py.
Run the script using a Python interpreter in your terminal.
Follow the on-screen instructions to guess the correct number between 1 and 6.
You have 3 attempts to guess the correct number.
Enter your guess when prompted. Make sure your input is a valid number between 1 and 6.
# Example Usage
python main.py
#Features
Simple and easy-to-understand gameplay.
Customizable attempts: You can adjust the number of attempts allowed by modifying the loop in the code.
Interactive splash screen: A welcoming splash screen greets players when they start the game.
Code Overview

#The game is implemented in Python and consists of a single script, main.py. Here's a brief overview of how the code works:

The print_splash_screen() function displays a splash screen with a welcome message.
A random number between 1 and 6 is generated using the random.randint() function.
Players have 3 attempts to guess the correct number.
A loop iterates through the attempts, prompting the user to enter their guess.
Input validation ensures that only valid numeric guesses are accepted.
If the guess is correct, the player wins and the game ends.
If the guess is incorrect, the player receives feedback on whether their guess was too high or too low.
If the player exhausts all attempts without guessing the correct number, they lose and the game ends.

# Contributions
Contributions to improve the game are welcome! If you have any ideas for new features, enhancements, or bug fixes, feel free to submit a pull request or open an issue on GitHub.
