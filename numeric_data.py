#🛠 How to Use Numeric Data
# Basic Math Operations, Python can do math just like a calculator:

a = 10
b = 3

print(a + b)  # Addition → 13
print(a - b)  # Subtraction → 7
print(a * b)  # Multiplication → 30
print(a / b)  # Division → 3.333...
print(a // b) # Floor division → 3 (no decimals)
print(a % b)  # Modulus → 1 (remainder)
print(a ** b) # Exponent → 1000 (10 to the power of 3)

#Type Checking
#You can check what kind of number you're working with:

x = 5
print(type(x))  # <class 'int'>

y = 3.14
print(type(y))  # <class 'float'>

#Convert Between Types
#Sometimes you need to switch between int and float:

x = 5
print(float(x))  # 5.0

y = 3.99
print(int(y))    # 3 (cuts off the decimal)

#Use in Real-Life Examples
#Let’s say you’re calculating the total cost of items:

price = 19.99
quantity = 3
total = price * quantity
print("Total cost:", total)  # Total cost: 59.97