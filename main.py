import random


def print_splash_screen():
  print("*********************************************************")
  print("*                                                       *")
  print("*              Welcome to EDX'S                         *")
  print("*                  Terminal Number Game                 *")
  print("*                                                       *")
  print("*********************************************************")


# random number between 1 and 6
number = random.randint(1, 6)

print_splash_screen()
print("You have 3 attempts to guess the correct number between 1 and 6.")

# this is the Loop to = 3 attempts
for attempt in range(3):
  print("Attempt", attempt + 1)
  guess = input("Enter your guess: ")

  if not guess.isdigit():
    print("Invalid input. Please enter a valid number.")
    continue

  guess = int(guess)

  if guess == number:
    print("Congratulations! You guessed correctly!")
    break  # if the guess is correct end the program
  elif guess < 1 or guess > 6:
    print("Please enter a number between 1 and 6.")
  elif guess > number:
    print("Your guess is too high.")
  else:
    print("Your guess is too low.")
else:
  print("Sorry, you've used all your attempts. The number was", number)
