# --- Lambda Functions ---
print("\n--- Lambda Functions ---")
add = lambda a, b: a + b
print("Sum:", add(3, 5))  # Output: 8

square = lambda x: x * x
print("Square of 4:", square(4))  # Output: 16

# --- map() Function ---
print("\n--- map() Function ---")
numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# --- filter() Function ---
print("\n--- filter() Function ---")
even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

# --- reduce() Function ---
print("\n--- reduce() Function ---")
from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print("Product of all numbers:", product)

# --- Mini Challenges ---

# Challenge 1: Use map() to convert temperatures from Celsius to Fahrenheit
print("\n--- Challenge 1 ---")
celsius = [0, 10, 20, 30]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print("Fahrenheit:", fahrenheit)

# Challenge 2: Use filter() to get numbers greater than 10
print("\n--- Challenge 2 ---")
values = [5, 10, 15, 20]
greater_than_10 = list(filter(lambda x: x > 10, values))
print("Greater than 10:", greater_than_10)

# Challenge 3: Use reduce() to find the maximum number
print("\n--- Challenge 3 ---")
nums = [4, 8, 2, 10, 5]
max_num = reduce(lambda x, y: x if x > y else y, nums)
print("Max number:", max_num)