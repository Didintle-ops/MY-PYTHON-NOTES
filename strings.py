#strings

message = "hello world"
print(message)

#advanced concepts in strings [postive indexing, negative indexing, slicing]
#positive indexing starts from 0

word = "Python"
print(word[0])  # P
print(word[1])  # y

#negative indexing starts from -1

word = "Python"
print(word[-1])  # n (last letter)
print(word[-2])  # o

#slicing, Slicing (Grab a Piece of the String)

word = "Python"
print(word[0:3])  # Pyt
print(word[2:])   # thon

#length of a string

word = "Python"
print(len(word))

sentence = "I love coding!"
print(len(sentence))

name = "Elephant"
print("Your name has", len(name), "letters!")

#built-in methods 
#Change Case .upper() – Make everything UPPERCASE

text = "hello"
print(text.upper())  # HELLO

#Change Case .lower() – Make everything lowercase
text = "HELLO"
print(text.lower())  # hello

#Change Case .title() – Capitalize First letter uppercase, rest lowercase
text = "python is fun"
print(text.capitalize())  # Python is fun

#.title() – Capitalize every word
text = "i love python"
print(text.title())  # I Love Python

#🧩 Split & Join
#.split() – Break a string into pieces
text = "apple,banana,cherry"
print(text.split(","))  # ['apple', 'banana', 'cherry']

#.join() – Glue pieces back together
words = ["apple", "banana", "cherry"]
print(", ".join(words))  # apple, banana, cherry

#🧼 Clean Up Text
#.strip() – Remove spaces from both ends
text = "   hello   "
print(text.strip())  # "hello"


#.lstrip() – Remove spaces from the left
text = "   hello"
print(text.lstrip())  # "hello"


#.rstrip() – Remove spaces from the right
text = "hello   "
print(text.rstrip())  # "hello"

#🔍 Search & Replace
#.find() – Find the position of a word/letter
text = "banana"
print(text.find("n"))  # 2


#.replace() – Swap one word/letter for another
text = "I like cats"
print(text.replace("cats", "dogs"))  # I like dogs