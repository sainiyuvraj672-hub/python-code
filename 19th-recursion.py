#  Recursion
# 1. Recursion is a process in which a function calls itself as a subroutine.
# 2. This allows the function to be repeated several times, as it can call itself during its execution.
# 3. Each time the function calls itself, it is called a recursive call.
# 4. The function that calls itself is called a recursive function.
# 5. The recursion process continues until a base case is met, at which point the function
#    stops calling itself and returns a value.
# 6. Recursion is a common mathematical and programming concept.
# 7. It can be used to solve problems that can be broken down into smaller, similar problems.
# 8. Recursion is often used in algorithms such as sorting and searching.
# 9. It can also be used to traverse data structures such as trees and graphs.
# 10. Recursion can be more elegant and easier to understand than iterative solutions for some problems.
# def show (n):
#     if (n==0):
#         return 0
#     print(n)
#     show(n-1)
#     print("End")
# show( 6)


#  factorial using recursion
# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     return (n* fact(n-1))
# print(fact(3))



#  fibonacci series using recursion

# def fib(n):
#     if(n==0):
#         return 0
#     elif(n==1):
#         return 1
#     else:
#         return (fib(n-1)+fib(n-2))
    
# n = fib(int(input("Enter the number:")))
# for i in range (n):
#     print(fib(i))


# natural number using recursion
# def natural (n):
#     if(n==0):
#         return 0
#     else:
#         return (natural(n-1)+n)
# print(natural(7))  # Output: 15

# print list using  recursion
def print_list(list, idx =0):
    if idx ==len(list):
        return
    print(list[idx])
    print_list(list, idx+1)

fruits = ["apple", "banana", "cherry","orange", "kiwi"]
print_list(fruits)