# Mr. Zerr, 1/14/26, Simple Guessing Game version 2

# Imports
import random as r

# variables/CONSTANTS
guesses_taken = 0
max_guesses = 3
secret_num = r.randint(1,10)
# secret_num = 5
win_lose = "lose"

# main code
print("Simple Guessing Game")
print("Rules/Goals: You need to guess the secret number in 3 guesses.")

while guesses_taken < max_guesses:
    guess = int(input("Please guess a number between 1-10. "))
    
    #Check the guess
    if guess > secret_num:
        print("Guess too high, guess again.")
        guesses_taken += 1
    elif guess < secret_num:
        print("Guess too low, guess again.")
        guesses_taken += 1
    elif guess == secret_num:
        print("You win!")
        win_lose = "win"
        break
    else:
        print("Error line - check guess")
        
if win_lose == "lose":
    print("Sorry you lost the game, please try again.")
else:
    print("Yay! Please come again.")
