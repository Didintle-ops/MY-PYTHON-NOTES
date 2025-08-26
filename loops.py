#🔁 What Is a Loop?
#A loop is like telling Python: “Hey, do this thing again and again until I say stop.”

#There are two main types of loops:

#Loop Type	What It Does	Example Use Case
#for-Loops a set number of times-Go through a list of names
#while-Loops as long as a condition is true-Keep asking until user says "stop"

#🔹 for Loop – Count or Repeat
#A for loop repeats a block of code a specific number of times.
#Example:
for i in range(5):
    print("Hello", i)
#This prints:
#Hello 0
#Hello 1   
#Hello 2  
#Hello 3  
#Hello 4

#🎒 Looping Through a List
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print("I like", fruit)
    
#This prints:
#I like apple
#I like banana
#I like cherry 

#🔸 while Loop – Keep Going Until Something Changes
count = 0

while count < 3:
    print("Counting:", count)
    count += 1
#This keeps looping until count is no longer less than 3.

#This prints:
#Counting: 0
#Counting: 1
#Counting: 2

#🛑 Loop Control Tools
#break → Stop the loop early

#continue → Skip this round, keep looping

for i in range(5):
    if i == 3:
        break
    print(i)
#This stops when i hits 3.

#this prints:
#0
#1
#2

#🎯 Mini Challenge
#Try this:

name = "Zola"

for letter in name:
    print(letter)
#It prints each letter of your name on a new line

#this prints:
#z
#o
#l
#a