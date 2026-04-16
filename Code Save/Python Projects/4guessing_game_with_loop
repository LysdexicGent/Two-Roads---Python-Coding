# Mr. Zerr, For Loops, 1/26/26

#imports
import random

#variables/CONSTANTS
max_num = 10
SECRET_NUM = random.randint(1, max_num)
players_guess = 0
rounds = 3

#main
# print("Number   Square")

# for num in range(1, 7):
#     square_num = num * num
#     print(f"{num}   {square_num}")
    
# print("Loop finished")

# guessing game
print(f"You are to guess a number between 1 and {max_num}.")
print(f"You get {rounds} guesses to get it right.")

for round in range(1, rounds + 1):
    players_guess = int(input(f"Enter a number from 1 to {max_num}: "))
    
    # check the number against SECRET_NUM
    if players_guess == SECRET_NUM:
        print(f"Hooray, you got it right, the number was {SECRET_NUM}!")
        break
    elif players_guess < SECRET_NUM:
        print("Guess higher.")
    else:
        print("Guess lower.")
        
print("Loop end")
