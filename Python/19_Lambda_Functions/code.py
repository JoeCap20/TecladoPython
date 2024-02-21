#Lambda function it is different becuase it has no name and is only used to return values 
#1. LAmbda key word 2.Parameter list 3.The : 4. return value without the return keyword
add = lambda x, y: x + y

print(add(5, 7))

#or which is not very common
print((lambda x, y: x + y)(5, 7))

#Useful lambda uses
def double(x):
    return x * 2

sequence = [1, 3, 5, 9]
#List comprenession is usually faster
doubled = [double(x) for x in sequence]
#Sometimes have to use map
doubled = list(map(double, sequence))

#this function rewritten as lambda which can be confusing
doubled = [(lambda x: x *2)(x) for x in sequence]
#Sometimes have to use map to make it more clear. have to turn map into a list in order to see output
doubled = list(map(lambda x: x * 2, sequence)) 

