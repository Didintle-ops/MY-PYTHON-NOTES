# 📘 Python Exception Handling – Notes

# 🔹 What Is an Exception?
# An exception is an error that occurs during program execution.
# Python lets you handle exceptions to prevent your program from crashing.

# 🔹 Common Exceptions
# ZeroDivisionError      → Raised when dividing by zero
# ValueError             → Raised when a function gets an invalid value
# TypeError              → Raised when an operation is applied to the wrong type
# FileNotFoundError      → Raised when a file operation fails due to missing file
# IndexError             → Raised when accessing an invalid index in a list

# 🔹 Basic Syntax
try:
    # Code that might cause an error
    pass  # placeholder to avoid syntax error
except ExceptionType:
    # Code to run if error occurs
    pass

# Optional blocks:
# else → runs if no error occurs
# finally → always runs (useful for cleanup)

# 🔹 Example 1: Handling Division by Zero
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
# 🔹 Example 2: Handling Invalid Input
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid number.")

# 🔹 Example 3: Using finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("This runs no matter what.")

# 🔹 Best Practices
# ✅ Be specific with exception types
# ✅ Use finally for cleanup (e.g., closing files)
# ✅ Avoid silent failures (don’t use empty except blocks)
# ✅ Log errors when needed for debugging

# 🔹 Summary of Keywords
# try     → Wraps risky code
# except  → Catches and handles errors
# else    → Runs if no error occurs
# finally → Always runs (even if error happens)


# 📘 Python Exception Handling – else Block Notes

# 🔹 What is the 'else' block in try-except?
# The 'else' block runs ONLY if no exception was raised in the try block.
# It's useful for separating error handling from success logic.

# 🔹 Syntax Overview
try:
    # Code that might raise an exception
    pass
except SomeError:
    # Code that runs if an exception occurs
    pass
else:
    # Code that runs only if no exception occurs
    pass
finally:
    # Code that runs no matter what (optional)
    pass

# 🔹 Example 1: Valid input with else
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid input. Please enter a number.")
else:
    print(f"Thanks! You entered: {age}")

# 🔹 Example 2: File reading with else
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found.")
else:
    print("File read successfully.")
    print(content)
finally:
    print("Execution complete.")

# 🔹 Why use 'else'?
# ✅ Keeps success logic separate from error handling
# ✅ Improves readability and structure
# ✅ Avoids running code that depends on successful try block

# 🔹 Summary
# try     → Wrap risky code
# except  → Handle specific errors
# else    → Run if no error occurs
# finally → Always run (cleanup, logging, etc.)

# 🔹 Best Practices
# - Use 'else' for code that should only run when no exception occurs
# - Avoid putting too much logic in the try block
# - Keep exception handling specific and meaningful

