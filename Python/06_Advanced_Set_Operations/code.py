friends = {"Bob", "Jo", "Jimbo"}
abroad = {"Jo", "Jimbo"}

#Difference takes one set and removes the elements from the other set from it
local_friends = friends.difference(abroad)
# #This line below will give an empty set which looks like set() when printed out
# local_friends = abroad.difference(friends)
print(local_friends)

local = {"Bob"}
abroads = {"Jo", "Jimbo"}
#Union unites two sets and gives the total of both
friendz = local.union(abroads)
print(friendz)

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}
#Intersection is what both of the sets have in common
both = art.intersection(science)
print(both)