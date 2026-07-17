#if statement is a conditional statement that allows you to execute a block of code only if a specified condition is true
#    The `if` statement is used to execute a block of code if a condition is true
#    The `else` statement is used to execute a block of code if the condition is false

age= int(input("Enter your age:"))

if age>=100:
    print("You are too old to sign-up!")
elif age>=18:
    print("You can sign-up!")
elif age<0:
    print("You are not born yet!")
else:
    print("You must be 18+ to sign-up!")


# Response =input("would u like a food (Y/N):")

# if Response == "Y":
#     print("have some food!")
# else:
#     print("No food for you!")

# online = True
# if online:
#     print("this User is online!")
# else:
#     print("this User is offline!")
