# ✅ What is a Tuple?
# A tuple is an ordered, immutable collection of items.
# You can store multiple values in a single variable.
# Once created, you cannot change, add, or remove items.

# ✅ Tuple Syntax
my_tuple = (1, 2, 3)  # Standard tuple with integers
mixed_tuple = ("apple", 3.14, True)  # Tuple with mixed data types

# ✅ Accessing Tuple Items
print(my_tuple[0])  # Output: 1 (first item)
print(mixed_tuple[2])  # Output: True

# ✅ Tuple with One Item
# IMPORTANT: You must include a comma to make it a tuple
single_item = ("hello",)
print(type(single_item))  # Output: <class 'tuple'>

# ✅ Nested Tuple
nested = (1, (2, 3), 4)
print(nested[1])  # Output: (2, 3)

# ✅ Tuple Unpacking
person = ("Alice", 25, "Engineer")
name, age, job = person
print(name)  # Output: Alice
print(age)   # Output: 25
print(job)   # Output: Engineer

# ✅ Looping Through a Tuple
colors = ("red", "green", "blue")
for color in colors:
    print(color)

# ✅ Immutability Example
# The following line would cause an error:
# colors[0] = "yellow"  # ❌ TypeError: 'tuple' object does not support item assignment

# ✅ Tuple Functions
print(len(colors))       # Output: 3
print(colors.count("red"))  # Output: 1
print(colors.index("green"))  # Output: 1

# ✅ When to Use Tuples
# - When data should not change
# - For faster performance than lists
# - As keys in dictionaries (if tuple contains only immutable items)

# ✅ Bonus: Tuple vs List
# List: mutable, uses []
# Tuple: immutable, uses ()

# Example:
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)