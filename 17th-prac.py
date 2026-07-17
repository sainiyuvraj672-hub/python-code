# print the length of list.

# cities = ["Jaipur", "Agra", "Delhi", "Mumbai", "Bangalore"]
# heroes = ["Batman", "Superman","Ironman", "Spiderman", "Ironman", "Thor"]

# def print_length(list):
#     print(len(list))
# print(len(heroes))

# # 
# def print_length(list):
#     for item in list:
#         print(item , end = " ")

# print(cities)
# print(heroes)

# factorial

# n = 5
# def fact (n):
#     fact = 1
#     for i in range (1,n+1):
#         fact *= i
#     print(fact)
# fact(5)


# money conversion
# def convert (usd_val):
#     inr_val = usd_val *83
#     return inr_val
# # after_conversion = convert(int(input( "Enter the value in USD: ")))
# # print(" The value in INR is: ", after_conversion)

# after_conversion = convert(2.5)
# print(f"the value in inr is{after_conversion}")


# string function 


# def string_function (name):
#     if len(name)% 2 == 0:
#         return "even"
#     else:
#         return "odd"

# name = string_function (input("enter the name:"))
# print((name))

# calculator by using function 
# def add (a,b):
#     return a+b
# def sub (a,b):
#     return a-b
# def mul (a,b):
#     return a*b
# def div (a,b):
#     if b==0:
#         return "Divisor cannot be zero"
#     else:
#         return (a,b)
# def avg (a,b):
#     return (a+b)/2

# # user input 

# print("chosse the operation:\n"
#       "1 Addition\n"
#       "2 Subractionnn"
#       "3 Multiplication\n"
#       "4 Division\n"
#       "5 Average\n")
# chosse = input("enter the operation from 1 to 5:")
# a = float(input("enter the first number:"))
# b = float(input("enter the second number:"))
# # let call the function based on user input

# if chosse == "1":
#     print(f"The addition of {a} and {b} is {add(a,b)}")
# if chosse == "2":
#     print(f"The subtraction of {a} and {b} is {sub(a,b)}")
# if chosse == "3":
#     print(f"The multiplication of {a} and {b} is {mul(a,b)}")
# if chosse == "4":
#     print(f"The division of {a} and {b} is {div(a,b)}")
# if chosse == "5":
#     print(f"The average of {a} and {b} is {avg(a,b)}")
# else:
#     print("Invalid choice")


# table of number using function
# def num_table (n):
#     for i in range (1,11):
#         print(f"{n}*{i} = {n*i}")
# num = num_table (int(input("enter the number:")))
# print(num)

# def fact_num (n):
#     fact = 1
#     for i in range(1,n+1):
#      fact*=i
#     return fact

# result = fact_num(int(input( "enter the number: ")))
# print(result)

# def strg_fun (name):
#     if len(name)%2 == 0:
#         return "even "
#     else:
#         return "odd "
# name = input("enter the name:")
# print(strg_fun(name))



# def table (n):
#     for i in range (1,11):
#         print(f" {n}*{i} = {n*i}")
# num = table(int(input(" enter the number: ")))
# print(num)



# def fact (n):
#     fact = 1
#     for i in range (1,n+1):
#      fact*=i
#     return fact
    
# number = fact(int(input("enter the number:")))
# print(number) 


# def total_num (n):
#     total=0
#     for i in range(1,n+1):
#      total+=i
#     return total
# num = total_num(int(input("enter the number: ")))
# print(num)


# def convert (Usd_val):
#     Inr_val = Usd_val*87.59
#     return Inr_val
# after_conv = convert(float(input("Enter the amound in usd:$ ")))
# print(f"after conversion the amount in Inr is :{round(after_conv,2)}₹5")

# fact= 1
# for i in range (4,0,-1):
#     fact *=i

# print(fact)  # output: 3628800

# n = 5
# sum = 0
# for i in range (1,n+1):
#     sum +=i
# print(sum)  