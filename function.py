# my_functions.py

# 🧁 Function 1: Make Coffee
# This function prints the steps to make coffee
def make_coffee():
    print("Boil water")
    print("Add coffee powder")
    print("Pour water into cup")
    print("Stir and enjoy!")

# 🧑‍🤝‍🧑 Function 2: Greet Someone
# This function takes a name and prints a greeting
def greet(name):
    print("Hello " + name + "! Have a great day.")

# ➕ Function 3: Add Two Numbers
# This function takes two numbers and returns their sum
def add_numbers(a, b):
    return a + b

# 🧪 Testing the functions
# These lines run the functions to see the output

make_coffee()           # Runs the coffee-making steps
greet("Thabo")          # Greets Thabo
greet("Aisha")          # Greets Aisha

result = add_numbers(5, 3)  # Adds 5 and 3
print("The result is:", result)  # Prints the result

# factorial_function.py

# 📘 This function calculates the factorial of a number
def factorial(n):
    result = 1  # Start with 1 because multiplying by 0 gives 0
    for i in range(1, n + 1):  # Loop from 1 to n
        result *= i  # Multiply result by each number
    return result  # Return the final result

# 🧪 Let's test it
print("5! =", factorial(5))  # Should print 120
print("3! =", factorial(3))  # Should print 6
print("0! =", factorial(0))  # Should print 1 (by definition)
print("1! =", factorial(1))  # Should print 1
