#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinkng of a number between 1 and 100")
the_number = randint(1, 101)
# print(the_number)
all_attemps = [5, 10]
difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")


def set_difficulty():
    if difficulty == 'easy':
        return all_attemps[1]
    else:
        return all_attemps[0]


attemps = set_difficulty()


def guess_number(attemps):
    while attemps > 0:
        print(f"You have {attemps} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        if user_guess > the_number:
            print("Too high.")
        elif user_guess < the_number:
            print("Too low. ")
        else:
            print(f"You got it! The answer was {user_guess}.")
            return
        attemps -= 1
        if attemps != 0:
            print("Guess again.")
    print("You've run out of guesses, you lose.")


guess_number(attemps)
