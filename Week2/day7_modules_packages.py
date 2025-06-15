# --- Python Modules & Packages ---

# --- Built-in Modules ---

# math module
import math
print("\n--- math Module ---")
print("Square root of 16 is:", math.sqrt(16))
print("Factorial of 5 is:", math.factorial(5))

# random module
import random
print("\n--- random Module ---")
print("Random number (1 to 6):", random.randint(1, 6))  # Simulates dice roll

# os module
import os
print("\n--- os Module ---")
print("Current working directory:", os.getcwd())

# --- Using 'from ... import ...' ---
from math import pi
print("\nUsing 'from ... import ...'")
print("Value of pi is:", pi)

# --- Using 'as' for aliasing ---
import random as r
print("\nUsing alias 'r' for random")
print("Random choice from list:", r.choice(['red', 'blue', 'green']))

# --- Creating Your Own Module ---
print("\n--- Custom Module ---")

# Suppose you create a file named mymodule.py in Week2/ with:
# def greet(name):
#     return f"Hello, {name}!"

# Then you can import it like this:
import mymodule
print(mymodule.greet("Pranav"))

# --- 🧠 Mini Challenges ---

# Challenge 1: Use math module to find power and floor
print("\nChallenge 1:")
print("3 to the power of 4 is:", math.pow(3, 4))
print("Floor of 3.7 is:", math.floor(3.7))

# Challenge 2: Simulate a dice roll 5 times
print("\nChallenge 2:")
for i in range(5):
    print(f"Roll {i+1}: {random.randint(1, 6)}")

# Challenge 3: Use your own module to print a custom message
print("\nChallenge 3:")
print(mymodule.greet("AI/ML Explorer"))
