friends = ["Bob", "Jo", "Jimbo", "Sally"]

# for friend in friends:
for friend in range(4):
    print(f"{friend} is my friend.")

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

#This below is one way but can be easily used with the Sum function
for grade in grades:
    total += grade

print(total / amount)

#How to use the sum function
grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)
