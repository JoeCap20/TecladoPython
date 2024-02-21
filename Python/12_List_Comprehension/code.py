# #The long most traditional way of doing it
# numbers = [1, 3, 5]
# doubled = []

# for num in numbers:
#     doubled.append(num * 2)

# #Quicker way that python has to do is comprehension
# numbers = [1, 3, 5]
# # doubled = [num * 2 for num in numbers]
# doubled = [x * 2 for x in numbers]
# print(doubled)


# #Traditional way of doing it
# friends = ["Bob", "Jo", "Sam", "Jimbo", "Susan"]
# starts_s = []

# for friend in friends:
#     if friend.startswith("S"):
#         starts_s.append(friend)
# print(starts_s)

#Faster way of doing it by comprehension
friends = ["Bob", "Jo", "Sam", "Jimbo", "Susan"]
starts_s = [friend for friend in friends if friend.startswith("S")]
print(starts_s)
