#this is how we create are own function and it is a callable variable and can be executed
def hello():
    print("Hello!")

#In order to call the function you have to do the below code
hello()

#defining another function
print("Welcome to the age in seconds program!")

def user_age_in_seconds():
    user_age = int(input("Enter your age: "))
    age_seconds = user_age * 365 * 24 * 60 * 60
    print(f"Your age in seconds is {age_seconds}")

user_age_in_seconds()

print("Goodbye!")

#Things to not do when working with functions 
#1.Do not reuse names
#The second print is no longer used as a normal print
def print():
    print("Hello, World!")
#2 Do not reuse variable in the same function becuase you will be defining a new vaiable. 
#Cannot use variable in same line being defined in also called as "shadowing a vairable"
firends = ["Jo", "Jimbo"]

def add_friend():
    friend_name = input("Enter your friend name: ")
    friends = friends + [friend_name]

add_friend()
# #3. cannot call a function before it is defined
# say_hello()

# def say_hello():
#     print("Hello!")

#Put global variable at the top
friends = []

def add_friend():
    friends.append("Joo")

add_friend()

print(friends)
