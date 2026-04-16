# Mr. Zerr, 11/10, Simple Number Guessing Game
"""Pseudocode:
START
    PRINT "Guess the number game."
    PRINT "You will have 2 guesses."
    secret_num = random from 1-5
    guess = 0
    PROMPT "Guess the number between 1-5."
    INPUT guess
    IF guess == secret_num
        PRINT "You Win!"
    ELSE
        PRINT "Guess again."
        PROMPT "Guess the number between 1-5."
        INPUT guess
        IF guess == secret_num
            PRINT "You Win!"
        ELSE
            PRINT "You lose."
END
"""

# Main Code
# Imports
import random as rd

# variables/CONSTANTS
guess = 0
secret_num = rd.randint(1, 5)
# TODO: remove following after debugging
#print(secret_num)
# END TODO

# instructions
print("Guess the number game.")
print("You will have 3 guesses.")

# inputs and checks
guess = int(input("Guess the number between 1-5. "))
if guess == secret_num:
    print("You Win!")
else:
    print("Guess again.")
    guess = int(input("Guess the number between 1-5. "))
    if guess == secret_num:
        print("You Win!")
    else:
        print("Wrong Number.")
        print("Guess again.")
        guess = int(input("Guess the number between 1-5. "))
        if guess == secret_num:
            print("You Win!")
        else:
            print("You lose!")
