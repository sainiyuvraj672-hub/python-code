# Logical operators in Python are used to combine conditional statements. They allow you to perform logical operations on boolean values (True or False). The three main logical operators in Python are:

# and: Returns True if both statements are true.
# or: Returns True if at least one of the statements is true.
# not: Reverses the result, returning True if the statement is false and vice versa.

# or operator
# temp = 38
# its_raining = False
# if temp<35 or temp>0 or its_raining:
#     print("the outdoor event is cancledd")
# else:
#     print("the outdoor event is still scheduled")

# and operator

temp = 28
its_sunny = False
if temp>=28 and its_sunny:
    print("it is hot outside 🥵.")
    print("it is sunny outside ☀️")
elif temp<=0 and its_sunny:
    print("it is cold outside ❄️")
    print("it is cloudy outside ☁️")  
elif 28> temp >0 and its_sunny:
    print("it is warm outside 🌞")
    print ("it is SUNNY ☀️")

# not operator

if temp>=28 and not its_sunny:
    print("it is hot outside 🥵.")
    print("it is Cloudy ☁️")
elif temp<=0 and not  its_sunny:
    print("it is cold outside ❄️")
    print("it is cloud ☁️")  
elif 28> temp >0 and not  its_sunny:
    print("it is warm outside 🌞")
    print ("it is SUNNY ☀️")
