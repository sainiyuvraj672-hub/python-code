#A while loop in Python is a control flow statement that allows code to be executed repeatedly based on a given condition.
#  The loop continues to execute as long as the condition evaluates to True.
#  Once the condition becomes False, the loop terminates.


# name = input("Enter your name:")

# while name == "":
#     print("you didn't enter your name:")
#     name = input("Enter your name:")
# else:
#     print(f"hello {name}")

# age = int(input("Enter your age:"))

# while age < 0:
#     print("Your age cant be nevative.")
#     age = int(input("Enter your age:"))

# print(f"Your age is:{age} ")


food= input("Enter the your favorite food:")

while not food== "q":
    print(f"yuo like food {food}")
    food = input("Enter the another food u like (q for exit):")

print ("bye")


# num = int(input(" Enter a # between 1-20: "))

# while num <1 or num >20:
#     print(f"{num} is not valid")
#     num = int(input(" Enter a # between 1-20: "))

# print(f"your number is {num}")