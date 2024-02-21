#This is a list of three elements uses ["", ""] lists can be modified so can add and remove
#Lists and tupiles also keep the order of elements
l = ["Bob", "Jo", "Billy"]
#This is a tuple and it uses () and they cannot be modified so cant add and remove
#Lists and tupiles also keep the order of elements
t = ("Bob", "Jo", "Billy")
#This is a set can add and remove but cannot have duplicate and will ignore it
#The order is not gurantened 
s = {"Bob", "Jo", "Billy"}

#Subscript notation it will give the element asked for
print(l[0])
print(t[1])

# #Subscript cannot be used on a set becuase the order changes
# print(s[0])

# #Changing and element with subscrpit for a list and cannot be done for a tupile or set
# l[0] = "Smith"
# print(l)

#add elements to a list using .append and will add to the end of it
l.append("Smith")
print(l)

#Remove elements from a list using .remove and will remove what you put in
l.remove("Bob")
print(l)

#Adding to a set uses .add uses .add becuase append means to add to the end but sets have no end
s.add("Smith")
print(s)