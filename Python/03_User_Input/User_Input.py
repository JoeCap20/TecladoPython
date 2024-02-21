#How to have a user input on the command prompt
name = input("Enter your name: ")
print(name)

#Doing MATHS with user input it will always give back a string 
size_input = input("How big is your house (in sqaure feet): ")
sqaure_feet = int(size_input)
sqaure_meters = sqaure_feet / 10.8
print(f"{sqaure_feet} square feet is {sqaure_meters:.2f} sqaure meters. ")