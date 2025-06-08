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
