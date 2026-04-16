#Mr. Zerr, 11/3, Intro to Python
print("Hello World!")

# Variable types
variable_string = "This is a string"
variable_int = 10
varible_list = ["This","is","a","list"]

print(variable_string)
print(variable_int)
print(varible_list)

# working with variables
input("Press Enter")
print(variable_int + 5)

count = 0
input("Press Enter")
while count < 10:
    count += 1
    print(count)
    
# IF/ELSE Statement
input("Press Enter")

if count < 10:
    print("Count is greater than or equal to 10")
elif count == 10:
    print("Count is 10")
else:
    print("This is the Else.")
