# Week2/day6_file_handling.py

print("--- File Handling in Python ---")

# 1. Create and initialize the file
with open("Week2/sample.txt", "w") as file:
    file.write("Line 1\nLine 2\nLine 3\n")

# --- .read() ---
print("\n--- .read() ---")
with open("Week2/sample.txt", "r") as file:
    content = file.read()
    print(content)

# --- .readline() ---
print("\n--- .readline() ---")
with open("Week2/sample.txt", "r") as file:
    line = file.readline()
    print(line.strip())

# --- .readlines() ---
print("\n--- .readlines() ---")
with open("Week2/sample.txt", "r") as file:
    lines = file.readlines()
    for l in lines:
        print(l.strip())

# --- .write() ---
print("\n--- .write() ---")
with open("Week2/sample.txt", "w") as file:
    file.write("This content replaced the previous one.\n")

# --- .writelines() ---
print("\n--- .writelines() ---")
lines = ["Alpha\n", "Beta\n", "Gamma\n"]
with open("Week2/sample.txt", "w") as file:
    file.writelines(lines)

# --- Append mode ---
print("\n--- Append mode ---")
with open("Week2/sample.txt", "a") as file:
    file.write("Appended this line.\n")

# --- 'r+' mode ---
print("\n--- 'r+' mode ---")
with open("Week2/sample.txt", "r+") as file:
    old = file.read()
    print("Old content:\n", old)
    file.seek(0, 2)  # Go to end of file
    file.write("Added with r+ mode\n")

# --- Challenge 1: Read file ---
print("\n--- Challenge 1: Read file ---")
with open("Week2/sample.txt", "r") as file:
    print(file.read())

# --- Challenge 2: Write user input ---
print("\n--- Challenge 2: Write user input ---")
user_input = "This is user input text."  # Simulating input()
with open("Week2/user_input.txt", "w") as file:
    file.write(user_input + "\n")

# --- Challenge 3: Append text ---
print("\n--- Challenge 3: Append text ---")
more_input = "Appending more text!"  # Simulating input()
with open("Week2/user_input.txt", "a") as file:
    file.write(more_input + "\n")
