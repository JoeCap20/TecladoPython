#This code below is for a while loop
number = 7
user_input = input("Would you like to play? (Y/n) ")

# while user_input != "n":
while True:
    user_input = input("Would you like to play? (Y/n) ")

    if user_input == 'n':
        break

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guess correctly!")
    elif abs(number - user_number) == 1:
        print("You are off by one.")
    else:
        print("You are wrong!")
