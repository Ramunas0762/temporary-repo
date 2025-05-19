#this will be a simple number guessing game
# the user will have to guess a number between 1 and 10
# if the user guess number is incorrect, the program will tell
# either "too high" or "too low"

print("welcome to the Number Guesing Game!")


import random

number_to_guess = random.randint(1, 10)



while parsed_guess != number_to_guess:
    user_input = input('Please enter your guess:  ')


print("You guessed: " + user_input)

try:
    parsed_guess = int(user_input)
except Exception:
    print("Invalid input, please enter a valid integer")
    exit()
if parsed_guess <1 or parsed_guess > 10:
    print("Your guess is out of range, please guess between 1-10")
elif parsed_guess < number_to_guess:
    print("Too low")
elif parsed_guess > number_to_guess:
    print("Too high")
else :
    print("You guessed correctly!")

print("The number was: " +str(number_to_guess))
