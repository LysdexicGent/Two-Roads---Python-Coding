#Mr. Zerr, Simple Escape Room, 1/28/26

#imports

#variables/CONSTANTS
escaped = "no"
rounds = 3

#main
print("You wake up in a locked room.")
print("You see three objects, a DOOR, a CABINET, and a WINDOW.")

for round in range(1, rounds + 1): #main gameplay loop
    print(f"You are on round {round}.")
    print(f"You have {rounds - round} rounds left.")
    
    #take player input
    choice = input("What do you want to check? (door / cabinet / window): ").lower() #.upper()
    
    #check choice against our choices
    #cabinet
    if choice == "cabinet" or choice == "c":
        print("You search the cabinet and find a small key.")
        escaped = "key"
        
    #door
    elif choice == "door" or choice == "d":
        #do they have the key?
        if escaped == "key":
            print("You unlock the door with the small key.")
            print("You escaped!")
            escaped = "yes"
            break
        else:
            print("The door is locked.")
    
    #window
    elif choice == "window" or choice == "w":
        print("The window is too small to escape through.")
        
    else:
        print("Invalid choice.")
        
if escaped == "yes":
    print("\nCongrats!")
else:
    print("\nYou did not escape in time.")
