# A string is a data type used in programming to represent a sequence of characters.
#  In most programming languages, including Python, strings are used to handle text.
#  Strings can be enclosed in single quotes or double quotes.

name = input("enter your name ")
# number = input("enter your number ")

result = len(name)
#  it will take the length of the string and return it

# result = name.find("u")
# it will return the index of the first occurrence of the specified value

# result = name.rfind("u")
# it will return the index of the last occurrence of the specified value

name =name.capitalize()
name = name.lower()
name = name.upper()

# name = name.isdigit()
# is digit() returns True if all characters in the string are digits, otherwise False.

# name = name.isalpha()
# is used to check if all characters in the string are alphabets.


# result = number.count(" ")
# it will return the number of occurrences of the specified value
print(result) 


# number = number.replace("-" , "")
# it will replace the specified value with the specified value

# result= number.count("0")
# print(number)

# print(help(str))

print(name)