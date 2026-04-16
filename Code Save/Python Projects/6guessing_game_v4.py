# Mr.Zerr, Loops Review, 2/2/26 - Simple guessing game version 3

#imports
import random as r

#variables/CONSTANTS
max_guesses = 3
secret_num = r.randint(1,10)
# secret_num = 5 #debugging tets
win_lose = "lose"

#main
print("Simple Guessing Game")
print("Rules/Goals: You need to guess the secret number in 3 guesses.")

for guesses in range(1, max_guesses + 1):
    # player input and error check
    while True:
        player_guess = input("Please guess a number from 1 to 10: ")
        if player_guess in "12345678910":
            player_guess = int(player_guess)
            break
        else:
            print("Please enter in a number from 1 to 10")
            
    #print(player_guess) #debugging code
    # check the guess against sec_num
    if player_guess < secret_num:
        print("Guess higher.\n")
    elif player_guess > secret_num:
        print("Guess lower.\n")
    elif player_guess == secret_num:
        print("You win!")
        win_lose = "win"
        break
    else:
        print("We should not see this error")
        
if win_lose == "lose":
    print("Sorry you lost the game, please try again.")
else:
    print("Yay! Please come again.")
