# input username not more than 12 letter
# must not contain space 
# must not contain special character
name = input("Enter your name: ")


if len(name) >12:
    print("Your Username can't be more than 12 letters.")
elif not  name.find(" ")==-1 :
    print("Your Username can't contain space.")
elif not name.isalpha():
    print("Your Username can't contain number or special character.")
else:
    print(f"Welcome{name}:")