# # #  shoping cart 

# # foods = []
# # prices = []
# # total = 0

# # while True:
# #     food = input("Enter a food to buy or Q for quit :")
# #     if food.lower() == "q":
# #         break
# #     else:
# #         price= float(input(f"Enter the Price of {food}: $"))
# #         foods.append(food)
# #         prices.append(price)

# # print("-----YOUR CART-----")
# # for food in foods:
# #     print(food , end = " ")

# # for price in prices:
# #     total+= price

# # print()

# # print("Your Total is $", total)


# contact list 

# contacts = []  

# while True:
#     print("\nContact book menu")
#     print("1. Add contact")
#     print("2. Delete contact")
#     print("3. Search contact")
#     print("4. Display all contacts")
#     print("5. Exit")

#     choice = input("Enter your choice: ")

#     if choice == '1':
#         name = input("Enter name: ")
#         phone = input("Enter phone number: ")
#         email = input("Enter Email-id: ")

#         contact = {  
#             "name": name,
#             "phone": phone,
#             "email": email
#         }
#         contacts.append(contact)  
#         print(f"{name} got saved successfully!")

#     elif choice == '2':  
#         name = input("Enter the name of the contact you want to delete: ")
#         found = False

#         for contact in contacts:
#             if contact["name"] == name:
#                 contacts.remove(contact)
#                 print(f"The contact {name} got deleted successfully!")
#                 found = True
#                 break 

#         if not found:  
#             print(f"Sorry, contact {name} not found!")

#     elif choice == '3':  
#         name = input("Enter the name of the contact you want to search: ")
#         found = False

#         for contact in contacts:
#             if contact["name"] == name:
#                 print(f"Contact found!\nName: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
#                 found = True
#                 break

#         if not found:
#             print(f"Sorry, contact {name} not found!")

#     elif choice == '4': 
#         if not contacts:
#             print("No contacts available!")
#         else:
#             print("\nContact list:")
#             for contact in contacts:
#                 print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

#     elif choice == '5':  
#         print("Exiting the program. Goodbye!")
#         break 

#     else:
#         print("Invalid choice! Please choose a valid option.")


contacts = []

while True:
    print("\nContact Manager Menu:")
    print("1. Add a contact")
    print("2. Delete a contact")
    print("3. Search a contact")
    print("4. Display all contacts")
    print("5. Exit the program")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email
        }
        contacts.append(contact)
        print(f"{name} added to the contact list!")

    elif choice == '2':
        name = input("Enter name of contact to delete: ")
        found = False

        for contact in contacts:
            if contact["name"] == name:
                contacts.remove(contact)
                print(f"{name} deleted from the contact list!")
                found = True
                break
            if not found:
                print(f"{name} not found in the contact list!")
    elif choice == '3':
        name = input("Enter the contact name u want to search: ")
        found = False
        
        for contact in contacts:
            if contact["name"] == name:
                print(f"Contact found name: {contact['name']}, phone: {contact['phone']}, email: {contact['email']}")
                found = True
                break
            if not found:
                print(f"Contact not found in the contact list!")
    elif choice == '4':
        if not contact:
            print("no contact in the list!!")
        else:
            for contact in contacts:
                print(f"Contact found name: {contact['name']}, phone: {contact['phone']}, email: {contact['email']}")
    elif choice == '5':
        print("Exiting the program...")
        break 
    else:
        print("Invalid choice. Please choose a valid option.")