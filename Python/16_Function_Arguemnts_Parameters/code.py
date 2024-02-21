def add(x, y):
    # pass #This means to do nothing
    result = x + y
    print(result)

add(5, 3)

#Function with no parameters adn returns no arguments but one was given
def say_hello():
    print("Hello")

say_hello("Bob")

#Would have to look like this and having a parameter means you must pass in an argument
def say_hello(name):
    print(f"Hello, {name}")

say_hello("Bob")

def say_hello(name, surname):
    print(f"Hello, {name} {surname}")
#These are named and key word arguments
say_hello(surname = "Bob", name = "Smith")
