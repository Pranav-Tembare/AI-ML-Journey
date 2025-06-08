# --- Functions ---
print("\nBasic Function:")
def greet():
    print("Hello, welcome to AI/ML journey!")

greet()

# --- Functions with Parameters ---
print("\nFunctions with Parameters:")
def greet(name):
    print(f"Hello, {name}!")

greet("Neo")

# --- Function with Return Value ---
print("\nFunction with Return Value:")
def add(a, b):
    return a + b

result = add(5, 6)
print("Sum is:", result)

# --- Default Parameters ---
print("\nDefault Parameters:")
def power(base, exponent=2):
    return base ** exponent

print(power(3))
print(power(2, 3))

# --- Keyword Arguments ---
print("\nKeyword Arguments:")
def describe(name, age):
    print(f"Name: {name}, Age: {age}")

describe(name="Aniket", age=23)

# --- ⚠️ Error Handling ---
print("\n⚠️ Error Handling:")
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero.")

# --- Mini Challenges ---

# Challenge 1: Function to check even or odd
def even_odd(num):
    if num % 2 == 0:
        return f"{num} is even."
    else:
        return f"{num} is odd."

print(even_odd(7))
print(even_odd(12))

# Challenge 2: Function to find max of two numbers
def max_of_two(a, b):
    return a if a > b else b

print("Max of 5 and 9:", max_of_two(5, 9))

# Challenge 3: Function to calculate factorial (with error handling)
def factorial(n):
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        for i in range(2, n + 1):
            fact *= i
        return fact

try:
    num = int(input("Enter a number to calculate factorial: "))
    print(f"Factorial of {num} is {factorial(num)}")
except ValueError:
    print("Invalid input! Please enter a valid integer.")