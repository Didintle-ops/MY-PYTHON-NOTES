#📘 modules_builtin.py – Notes
#🔹 What Are Built-in Modules?
#Built-in modules are included with Python by default.

#You don’t need to install them—just import and use.

#They provide ready-made functions for math, randomness, dates, system operations, and more.

#🔹 Common Built-in Modules
#Module	Purpose
#math	Advanced mathematical functions
#random	Generate random numbers or choices
#datetime	Work with dates and times
#os	Interact with the operating system
#sys	Access system-specific parameters

#🔹 How to Use Them
#python
#import module_name
#You can also import specific functions:

#python

#from module_name import function_name
#Or rename it for convenience:

#🧪 modules_builtin.py – Examples
#python
# modules_builtin.py

# 1. Math module
import math
print("Square root of 25:", math.sqrt(25))
print("Value of pi:", math.pi)
print("Factorial of 5:", math.factorial(5))

# 2. Random module
import random
print("Random integer between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice(['apple', 'banana', 'cherry']))

# 3. Datetime module
import datetime
now = datetime.datetime.now()
print("Current date and time:", now)
print("Today's date:", datetime.date.today())

# 4. OS module
import os
print("Current working directory:", os.getcwd())
print("List of files in directory:", os.listdir())

# 5. Sys module
import sys
print("Python version:", sys.version)
print("System path:", sys.path)