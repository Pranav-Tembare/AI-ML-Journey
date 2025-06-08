# --- If / Elif / Else ---
print("\n--- If / Elif / Else ---")
age = 18

if age >= 18:
    print("You're an adult.")
elif age > 13:
    print("You're a teenager.")
else:
    print("You're a child.")

# --- For Loop ---
print("\n--- For Loop ---")
for i in range(5):
    print("Loop number:", i)

# --- While Loop ---
print("\n--- While Loop ---")
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# --- Break ---
print("\n--- Break Example ---")
for i in range(5):
    if i == 3:
        break  # Stops the loop
    print(i)

# --- Continue ---
print("\n--- Continue Example ---")
for i in range(5):
    if i == 2:
        continue  # Skips this iteration
    print(i)

# --- Mini Challenges ---

# Challenge 1: Even or Odd
num = 7
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Challenge 2: Count 1 to 10, skip 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# Challenge 3: Stop at 7 using while loop
i = 1
while i <= 10:
    if i == 7:
        break
    print(i)
    i += 1

# Challenge 4: Grading system
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D or below")