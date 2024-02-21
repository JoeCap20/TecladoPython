users = [
    (0, "Jo", "password"),
    (1, "Bob", "bob123"),
    (2, "Jimbo", "longp4assword"),
    (3, "Susan", "1234"),
]

# #Mapping of user name to user information
# #gets the user name and associates the entire tuple for it
# username_mapping = {user[1]: user for user in users}

# print(username_mapping["Bob"])

# #if you didnt have mapping you would have to do
# for user in users:
#     if user[1] == "Bob":
#         print(user)

#Asking users to log in
username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping(username_input)

if password_input == password:
    print("Your details are correct!")
else:
    print("Your details are incorrect!")