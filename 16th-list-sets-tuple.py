# colection = single "variable" used to store multiple values
# list = []ordered collection of values that can be of any data type
# tuple = ()ordered collection of values that can be of any data type, but cannot be changed
# set = {}unordered collection of value add and remove are allowed but duplicates are not

# fruits =["apple","banana","grapes","pomegrante"]
# print(fruits[1:4]) 
# for fruit in fruits:
#     print(fruit)
# print(dir(fruits))
# print(help(fruits))

# fruits[1]= "orange"

# for fruit in fruits:
#     print(fruit)  

# to add a new element in the list
# fruits.append("Orange")  # apend() is used to add a new item in the list 
# fruits.append("Mango")
# print("my fav fruits are ",fruits)
# # to remove a element from the list
# fruits.remove("Orange")
# print("my fav fruits are ",fruits)
# # to insert a element at a specific position in the list
# fruits.insert(2,"Water melon")
# print("my fav fruits are ",fruits)
# # to sort the list in ascending order
# fruits.sort()
# print("my fav fruits are ",fruits)
# # to sort the list in descending order
# fruits.sort(reverse=True)
# print("my fav fruits are ",fruits)
# to clear the list
# fruits.clear()
# print("my fav fruits are ",fruits)  
# to get the index of the element in the list
# print(fruits.index("grapes")).


# Sets

# fruits ={"Apple", "Banana", "Grapes", "Pomegrante"}
# print(fruits) 
# print(dir(fruits))
# add a new element in the set
# fruits.add("Water melon")
# print(fruits)
# remove a element from the set
# fruits.remove("Banana")
# print(fruits)  



# list = [1,2,2,5,6,8,3,2,5,4,1,2,5,6,5,8,1,2,3,6,4,5]
# U_list = []

# for i in list:
#     if i not in U_list:
#         U_list.append(i)
#         print(U_list)


a= [3, 6, 9, 3, 6, 3, 6, 8, 3, 9, 8, 6, 6]
u=[]
if(len(a)<2):
    print("invalid list")
else:
    for i in a:
        if i not in u:
            u.append(i)
u.sort(reverse= True)
print(u[1])  

