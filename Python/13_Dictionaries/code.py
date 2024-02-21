# friend_ages = {"Bob": 26, "Jo": 25, "Jimbo": 29}

# friend_ages["Jimbo"] = 20

# # print(friend_ages["Jo"])
# print(friend_ages)

# #A list of dictionaries
# friends = [
#     {"name": "Bob", "age": 26},
#     {"name": "Jo", "age": 25},
#     {"name": "Jimbo", "age": 29}
# ]

# # print(friends)
# print(friends[1]["name"])

# student_attendance = {"Jo": 105, "Jimbo": 98, "Sean": 55}

# for student, attendance in student_attendance.items():
#     print(f"{student}: {attendance}")

# if "Jo" in student_attendance:
#     print(f"Jo: {student_attendance['Jo']}")
# else:
#     print("Jo is not a student in this class.")

student_attendance = {"Jo": 105, "Jimbo": 98, "Sean": 55}

attendance_values = student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
