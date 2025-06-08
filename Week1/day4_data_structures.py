# --- Lists ---
print("Lists:\n(Ordered, mutable collections)")
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple
fruits.append("mango")  # add item
print(fruits)  # ['apple', 'banana', 'cherry', 'mango']

# --- Tuples ---
print("\nTuples:\n(Ordered, immutable collections)")
point = (10, 20)
print(point[0])  # 10

# --- Sets ---
print("\nSets:\n(Unordered, no duplicates)")
unique_numbers = {1, 2, 3, 2}
print(unique_numbers)  # {1, 2, 3}

# --- Dictionaries ---
print("\nDictionary:\n[Key-value pairs (used a lot in real projects)]")
student = {"name": "Raj", "age": 19}
print(student["name"])  # Raj
student["grade"] = "A"
print(student)

# --- Mini Challenges ---

# 1. List Challenge: Print all fruits in uppercase
print("\nChallenge 1: Uppercase Fruits")
for fruit in fruits:
    print(fruit.upper())

# 2. Tuple Challenge: Unpack and print x, y from a point
print("\nChallenge 2: Tuple Unpacking")
x, y = point
print(f"x = {x}, y = {y}")

# 3. Set Challenge: Add new number and print
print("\nChallenge 3: Set Add")
unique_numbers.add(4)
print(unique_numbers)

# 4. Dictionary Challenge: Loop through keys and values
print("\nChallenge 4: Student Info")
for key, value in student.items():
    print(f"{key}: {value}")