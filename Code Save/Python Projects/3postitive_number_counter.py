#Mr. Zerr, Positive Number Counter, 1/21/26

"""Pseudocode
START
    PRINT welcome message
    WHILE count < 5
        PROMPT user enter number
        INPUT num
        count + 1
        IF num > 0
            positive_number + 1
        ELSE
            PRINT negative number message
    
    PRINT total positive numbers
END
"""

#Imports

#variables/CONSTANTS
count = 0
positive_number = 0
num = 0
# 0 is a good default value for numbers. - " " is a good default value for strings

# Main
print("This is a positive number counter. You will enter in numbers and it will count positive numbers.")

# while loop for entering numbers
while count < 5:
    num = int(input("Please enter a number now: "))
    
    #TODO: Add in a error check to make sure the user doesn't enter a character besides a number.
    count += 1 #count = count + 1
    if num > 0:
        print("positive number")
        positive_number += 1
    else:
        print("Not a positive number.")
        
# end of program message
print(f"Your total positive numbers = {positive_number}.")
