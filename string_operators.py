#🔗 What Is String Concatenation?
#Concatenation means joining strings together — like gluing words side by side.

#🧪 Example:
# Let's join two strings together
first = "Hello"
second = "World"
result = first + " " + second
print(result)

#This prints:
# Hello World
#We used the + operator to combine the strings, and added " " (a space) in between

#🧠Combine with Variables
name = "Zola"
greeting = "Hello, " + name + "!"
print(greeting)

# This prints:
# Hello, Zola!

#⚠️ Watch Out!
#You can’t use + to combine a string with a number directly:

age = 25
# print("Age: " + age)  ❌ Error!

#You need to convert the number to a string first:
#print("Age: " + str(age))  ✅