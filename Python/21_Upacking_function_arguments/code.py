# def multiply(*args):
#     print(args)
#     total = 1
#     for arg in args:
#         total = total * arg

#     return total

# print(multiply(1, 3, 5))

# def add(x, y):
#     return x + y
# #The * passes one value for each parameter and need the same number on top and bottom
# nums = [3, 5]
# # or it can be
# #nums = {"x": 15, "y": 25}
# #print(add(x=nums["x"], y=nums["y"]))
# print(add(*nums))

def multiply(*args):
    # print(args)
    total = 1
    for arg in args:
        total = total * arg

    return total

#this means to collect all of positonal arguments in args and a named argument at the end 
def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid oeprator provided to apply()."
    
print(apply(1, 3, 6, 7, operator="*"))