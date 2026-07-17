# Calculator by using if else statement
import math
# operator = input("Enter operator (+, -, *, /, %):")

# A = float(input("Enter the no A:"))
# B = float(input("Enter the no B:"))

# if operator == "+":
#     result = A + B
#     print(f"The A+B is {round (result,2)}.")
# elif operator == "-":
#     result = A - B
#     print(f"The A-B is {round (result,2)}.")
# elif operator == "*":
#     result = A * B
#     print(f"The A*B is {round (result,2)}.")
# elif operator == "/":
#     result = A / B
#     print(f"The A/B is {round (result,2)}.")
# elif operator =="%":
#     result = A % B 
#     print(f"The A%B is {round (result,2)}.")
# else:
#     print("Invalid operator!")

# program to conver temp from celcius to fahrenheit or vice versa
unit = input("Is this temprature in Celsius and Ferhenite (C/F): ")
temp =float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9*temp /5 +32),1)
    print(f"The temprature is {temp}°F")
elif unit == "F":
    temp = round((temp-32 *5/9 ),1)
    print(f"The temprature is {temp}°C")

else:
    print("Invalid unit. Please enter C or F")



# ptogeram to convert your weight 
# import math
# weight =float(input("Enter your Weight:"))
# unit =input("Chosse your unit kilogram / pound (K/L):")

# if unit == "K":
#     weight =weight * 2.205
#     unit = "lbs."
# elif unit == "L":
#     weight =weight / 2.205
#     unit = "kgs."
# else :
#     print(f"{unit} was not valid")

# print(f"You're weight is {weight} {unit}")