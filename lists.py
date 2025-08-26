#🔹 What is a List?
#A list is a collection of items stored in a single variable. You can think of it like a row of boxes, each holding something—numbers, words, or even other lists.

my_list = ["1, 2, 3, 4, 5"]
#🔹 Key Properties
#Ordered: Items stay in the order you put them.

#Mutable: You can change the contents.

#Allows duplicates: Same value can appear more than once.

#Can hold mixed types: Numbers, strings, booleans, etc.


mixed_list = [42, "hello", True, 3.14]
#🧪 Common List Operations with Examples

#1. ✅ Creating a List
fruits = ["apple", "banana", "cherry"]

#2. 📦 Accessing Items
print(fruits[0])  # Output: apple

#3. ✏️ Changing Items
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

#4. ➕ Adding Items
fruits.append("orange")
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

#5. ❌ Removing Items
fruits.remove("cherry")
print(fruits)  # Output: ['apple', 'blueberry', 'orange']

#6. 🔢 Length of List
print(len(fruits))  # Output: 3

#7. 🔁 Looping Through a List
for fruit in fruits:
    print(fruit)
    
#8. 🧩 Slicing a List
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])  # Output: [20, 30, 40]

#9. 🔍 Sorting Operation
numbers = [8, 3, 1, 6, 2]
numbers.sort() #reverse=True for descending order
print(numbers)
#Output:

#[1, 2, 3, 6, 8] arranged in ascending order

#example, try out the following code snippets in your Python environment to see how lists work:

colors = ["red", "green", "blue"]
colors.append("yellow")
colors[1] = "purple"
colors.remove("red")
print(colors)