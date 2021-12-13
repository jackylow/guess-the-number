import random
from art import logo
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_number = random.randint(1, 100)
# print(computer_number)
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
if level == "easy":
    attempts = 10
else:
    attempts = 5
print(f"You have {attempts} attempts remaining to guess the number.")
game = True
while game:
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break
    user_number = int(input("Make a guess: "))
    if user_number > computer_number:
        print("Too high.\nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif user_number < computer_number:
        print("Too low.\nGuess again.")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif user_number == computer_number:
        print(f"You got it! The answer was {user_number}.")
        game = False
