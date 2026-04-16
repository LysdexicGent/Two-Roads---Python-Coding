# Mr. Zerr, 11/5, Simple Decisions
"""
START
    PRINT "Adding or Subtracting"
    PROMPT "DO you want + or -?"
    INPUT selection
    PROMPT "enter your two numbers"
    PRINT "If - selected, second num is subtracted"
    INPUT num1
    INPUT num2
    IF selection = +
        num1 + num2 = total
        PRINT total
    ELSE
        num1 - num2 = total
        PRINT total
    PRINT "END MESSAGE"
END
"""

# main code
# variables/CONSTANTS
num1 = 0
num2 = 0
total = 0
selection = " "

# taking input
print("Adding or Subtracting machine. If Subtracting then 2nd number is subtracted from 1st number.")
selection = input("Do you want x or /: ")
num1 = int(input("Input 1st number: "))
num2 = int(input("Input 2nd number: "))

# maths
if selection == "x":
    total = num1 * num2
    print(total)
else:
    total = num1 // num2
    print(total)
    
print("This is a exit message.")
