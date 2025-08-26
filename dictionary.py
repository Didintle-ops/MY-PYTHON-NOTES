# ✅ What is a Dictionary?
# A dictionary is a collection of key-value pairs.
# Each key is unique and maps to a value.
# Dictionaries are unordered (until Python 3.7+) and mutable.

# ✅ Dictionary Syntax
person = {
    "name": "Alice",
    "age": 25,
    "job": "Engineer"
}

# ✅ Accessing Values
print(person["name"])  # Output: Alice

# ✅ Adding a New Key-Value Pair
person["city"] = "Cape Town"
print(person)  # Output includes 'city': 'Cape Town'

# ✅ Updating a Value
person["age"] = 26

# ✅ Removing a Key-Value Pair
del person["job"]

# ✅ Using .get() Method (avoids error if key doesn't exist)
print(person.get("job"))  # Output: None

# ✅ Looping Through a Dictionary
for key in person:
    print(key, ":", person[key])

# ✅ Getting All Keys and Values
print(person.keys())    # Output: dict_keys(['name', 'age', 'city'])
print(person.values())  # Output: dict_values(['Alice', 26, 'Cape Town'])

# ✅ Checking if a Key Exists
if "name" in person:
    print("Name is present")

# ✅ Clearing the Dictionary
person.clear()
print(person)  # Output: {}

# ✅ Nested Dictionary
student = {
    "name": "John",
    "grades": {
        "math": 90,
        "science": 85
    }
}
print(student["grades"]["math"])  # Output: 90

# ✅ Dictionary from List of Tuples
pairs = [("a", 1), ("b", 2)]
dict_from_list = dict(pairs)
print(dict_from_list)  # Output: {'a': 1, 'b': 2}
# -------------------------------