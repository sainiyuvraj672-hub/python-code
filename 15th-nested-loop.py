# a loop where we create a another loop inside a loop
# we will use a for loop to iterate over a list of lists
#                outer loop
#                   inner loop

# a normal loop 
# for x in range (1,10):
#     print(x, end="-")

# a loop inside a loop
# for x in range (3):
#     print("outerr loop iteration no",x)
#     for y in range(10):
#         print(y, end=" ")
#     print("")


# make trinagle
rows= int(input("Enter a # of rows"))
columns = int(input("Enter a # of columns"))
symbols = input("Enter a # of symbols")

for x in range (rows):
    for y in range (columns):
        print(symbols, end="")
    print()

# in while loop

# i = 1
# while i<4:
#     print("the iteration no is ",i)
#     for x in range(10):
#         print(x)
#     print()
#     i+=1


# make trinagle by using while loop
# rows = int(input("Enter a # of rows"))
# columns = int(input("Enter a # of columns"))
# symbols = input("Enter a # of symbols")

# i =1
# while i<=rows:
#     for x in range(columns):
#         print(symbols, end="")
#     print()
#     i+=1


# for num in range (1,100):
#     for i in range(2,num):
#         if num%i ==0:
#             break
#     else:
#         print(num)