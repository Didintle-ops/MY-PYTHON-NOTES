# ✅ 1. Arithmetic Operators
# Used for basic math operations
x = 10
y = 3

print(x + y)  # Addition → 13
print(x - y)  # Subtraction → 7
print(x * y)  # Multiplication → 30
print(x / y)  # Division → 3.333...
print(x % y)  # Modulus → 1 (remainder)
print(x ** y) # Exponentiation → 1000
print(x // y) # Floor Division → 3

# ✅ 2. Assignment Operators
# Used to assign values to variables
a = 5
a += 2  # Same as a = a + 2 → 7
a *= 3  # Same as a = a * 3 → 21

# ✅ 3. Comparison Operators
# Used to compare values
print(x == y)  # Equal → False
print(x != y)  # Not Equal → True
print(x > y)   # Greater Than → True
print(x < y)   # Less Than → False
print(x >= y)  # Greater or Equal → True
print(x <= y)  # Less or Equal → False

# ✅ 4. Logical Operators
# Used to combine conditional statements
print(x > 5 and y < 5)  # True and True → True
print(x > 5 or y > 5)   # True or False → True
print(not(x > y))       # Not True → False

# ✅ 5. Identity Operators
# Used to compare memory locations
a = [1, 2]
b = a
c = [1, 2]

print(a is b)  # True (same object)
print(a is c)  # False (same content, different object)

# ✅ 6. Membership Operators
# Used to check if a value is in a sequence
colors = ["red", "green", "blue"]
print("red" in colors)     # True
print("yellow" not in colors)  # True
# -------------------------------