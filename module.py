#📘 Python Modules – Notes
#🔹 What is a Module?
#A module is a Python file (.py) that contains reusable code: functions, classes, or variables.

#Modules help organize code into logical sections and make it easier to maintain.

#🔹 Types of Modules
#Built-in Modules – Already included with Python (e.g., math, random, datetime)

#Custom Modules – Created by you to reuse your own code

#Third-party Modules – Installed using pip (e.g., numpy, requests)

#🔹 Why Use Modules?
#Keeps code organized

#Makes code reusable

#Helps with collaboration (different people can work on different modules)

#🔹 How to Use a Module
#Use the import keyword to bring a module into your program:

#python
#import module_name
#You can also import specific functions:

#python
#from module_name import function_name
#Or rename it for convenience:

#python
#import module_name as mn
#🔹 How to Create Your Own Module
#Create a new .py file (e.g., module.py)

#Define your functions or classes inside

#Import it into another file (e.g., main.py) and use the functions

#🧪 Example 1: module.py (Your Custom Module)
#python
# module.py

def greet(name):
    return f"Hello, {name}! Welcome to your custom module."

def add(a, b):
    return a + b