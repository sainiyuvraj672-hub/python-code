#Variables are containers for storing data values.
#Variables can be assigned a value and used throughout your program.
#Variables are case sensitive, so "var" and "Var" are two different variables.
#Variables do not need to be declared before they are used.

# name = "Yuvz"
# age = 20
# print(f"My Name is {name} and i'm a {age} year's old." )

#In Python, f-strings (formatted string literals) are a way to embed expressions inside string literals, using curly braces {}.

#strings
#Strings can be declared as single quotes, double quotes, or triple quotes.
x="20"
y="25"
print(f"the sum of {x} and {y} is {x+y}")

pi =3.142853
print(f"the value of pi is {pi:.2f}")
#The above code will print the sum, difference, product and division of x and y.

#integer
#Integer is a whole number, either positive, negative or zero.
#In Python, integers are not limited to 32 bits, they can be any size.

age = 20
quantity =65
no_of_persons  = 57
print(f"my age is {age}")
print(f"the items quantity is {quantity}")
print(f"the number of persons is {no_of_persons}")

#float
# float is a data type that represents a floating-point number, which is a number that has a decimal point. Floats are used to represent real numbers and can include both whole numbers and fractions.

price = 206.98
gpa = 6.95
print(f"the price of this item is ${price}")
print(f"my gpa of this year is {gpa}")


#booleans
#Boolean is a data type that can have one of two values: True or False.
#Boolean values are used to represent true or false conditions.

is_student = False
for_sale = True

if is_student:
    print("you're a student")
else:
    print("you're not a student")

if for_sale:
    print("this item is for a sale")
else:
    print("this item is not for a sale")