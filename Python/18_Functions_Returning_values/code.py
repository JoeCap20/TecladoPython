def add(x, y):
    return x + y

#Functions return none by default 
add(5, 8)
result = add(5, 8)
print(result)

#Another example
def divide(dividend, divisor):
    if divisor != 0:
        return dividend / divisor
    else:
        return "You fool!"

result = divide(15, 3)
print(result)