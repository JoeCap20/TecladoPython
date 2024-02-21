# # In string formatting it only takes what is in it even if changed later on
# name = "Bob"
# greeting = "Hello, Bob"

# print(greeting)

# name = "Jim"

# print(greeting)

# # Need to use an f string here but stays with it for the line above
# name = "Bob"
# greeting = f"Hello, {name}"

# print(greeting)

# name = "Jim"

# # This will print the latest name there
# name = "Bob"
# print(f"Hello, {name}")

# name = "Jim"
# print(f"Hello, {name}")

# # This is how we can define a template using .format()
# name = "Bob"
# greeting = "Hello, {}"
# with_name = greeting.format(name)

# print(with_name)

# How to create a longer string using .format()
longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Jimbo", "Friday")

print(formatted)