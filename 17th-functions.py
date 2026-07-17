# functions = a fuction is a block of code that perform a specific task. you can used it whenever you want by calling its name,
# which save u writiong the same code again and again.
# functions are used to make the code more readable and easier to understand.

# syntax of function in python

# def function_name(parameters):       keyword def is used to define a function in python 
#       instruction-1
#       instruction-2                  instruction
#       instruction-3
#       return value                   keyword retun give the result of the function


# to add 3 num is function 

def num3 (a,b,c):
    return (a+b+c)/3
result = num3(
    a = float(input(" enter the first number: ")),
    b = float(input(" enter the second number: ")),
    c = float(input(" enter the third number: "))
)
print(result)  
print(type(result))

# def avg (a,b,c):
#     sum = a+b+c
#     avg1 = sum/3
#     print(avg1)
#     return avg1

# avg (1,5,4)


# there are the 2 types of function 

# 1. built in function
# built in function are the function that are already defined in python
# we can use them without defining them
# example of built in function
# print() , len() , max() , min() , range() , type() , input

# 2. user defined function
# user defined function are the function that are defined by us
# we can use them after defining them

# def function_name(parameters):       keyword def is used to define a function in python 
#       instruction-1
#       instruction-2                  instruction
#       instruction-3
#       return value                   keyword retun give the result of the function

# default argument value
# we can assign a default value to the argument in the function definition
# if the argument is not passed in the function call, it will take the default value

# example of default argument value
# def cal (a=4 ,b=5):
#     return a*b
# result = cal()
# print(result)



