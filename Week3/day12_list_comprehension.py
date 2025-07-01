# --- Day 12: List Comprehensions ---

# 1. Basic list comprehension (Squares of numbers)
squares = [num ** 2 for num in range(1, 11)]
print("Squares from 1 to 10:", squares)

# 2. With condition (Even squares only)
even_squares = [num ** 2 for num in range(1, 11) if num % 2 == 0]
print("Even Squares:", even_squares)

# 3. Convert names to lowercase
names = ["Alice", "BOB", "Charlie"]
lower_names = [name.lower() for name in names]
print("Lowercase Names:", lower_names)

# 4. Filter only vowels from a list
letters = ["a", "b", "e", "i", "u", "x"]
vowels = [ch for ch in letters if ch in 'aeiou']
print("Vowels only:", vowels)

# 5. Convert USD to INR
dollars = [5, 10, 20]
inr_values = [usd * 83 for usd in dollars]
print("INR values:", inr_values)

# 6. Nested list flattening
matrix = [[1, 2], [3, 4]]
flattened = [num for row in matrix for num in row]
print("Flattened list:", flattened)
