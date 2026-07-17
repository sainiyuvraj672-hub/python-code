# conditional operator 
# a logical operation in programming that tests conditions in statements like if, while, or for loops

# age =14
# status = "Adult " if age >=18 else "Minor"
# print(status)

# num =24
# result = "Even" if num%2 == 0 else "odd"
# print (result)

# score =93
# result = "Excellent" if score>=90 else "Good" if score >= 75 else "Average" if score >= 50 else "Fail"
# print(result)

a=-58
b=-6
c=2

max_num = a if a>b and a>c else b if b>c else c and c if c>b else c>a 
print(max_num)

