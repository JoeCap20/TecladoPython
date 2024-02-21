#the parenthesis for a couple are only neccesary if python mght be confused on creating a tuple or another collection
z = (5, 11)
x, y = z

print(x, y)

#This is doing it in a list now
student_attendance = {"Jo": 105, "Jimbo": 98, "Sean": 55}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")


#A tuple with three values
people = [("Jo", 105, "Cybersecurity"), ("Jimbo", 98, "Chef"), ("Sean", 55, "Hobo")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

#How to do it when you dont care about a value use _
person = ("Jo", 42, "Chef")
name, _, profession = person

print(name, profession)

#Seperating into two lists
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)
