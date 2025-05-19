#this will be a simple number guessing game
# the user will have to guess a number between 1 and 10
# if the user guess number is incorrect, the program will tell
# either "too high" or "too low"

print("welcome to the Number Guesing Game!")


import random


number_to_guess = random.randint(1, 10)


user_input = input("Please enter your guess:  ")

print("You guessed: " + user_input)

