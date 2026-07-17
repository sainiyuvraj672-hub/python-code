# list = [1,4,9,16,25,36,49,64,81,49,100]
# x= 49

# idx =0
# for val in list:
#     if( val == x):
#         print("Number found at idx",idx)
#         break
#     idx+=1

# write all the even no between 1 to 100

# for i in range(0,101,2):
#     print(i)

# print("All the even no between 1 to 100 are: ",end="")


# # write all the even no between 1 to 100

# for i in range (1,100,2):
#     print(i)

# print("All the odd no between 1 to 100 are: ",end="")


# print a number between 1 -100

# num = range(1,101)

# for i in num:
#     print(i)

# print a number between 100 - 1

# num = range(100,0,-1)
# for i in num:
#     print(i)

# print the table 
num = int(input("Enter a number: "))
for i in range(1,11):
    print(f"{num} X {i} = {num*i}")

print(f"this is the table of {num}")


# print the sum of n number 
# n= 10
# sum =0
# for i in range (1,n+1):
#     sum += i

# print(f"The total of {n} is {sum}")

# print the fact of n number 

# n= int(input( "Enter a number: "))
# fact =1
# for i in range(1,n+1):
#     fact*= i

# print("the fact of n is ",fact)

# countdown 
# import time
# my_time = int(input("Enter your time in seconds"))

# for x in range(my_time,0,-1):
#     print(x)
#     # time.sleep(1)

# print("Times's up!!")