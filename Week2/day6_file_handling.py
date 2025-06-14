# --- Opening and reading a file ---

# Writing a sample text file first
with open('sample.txt', 'w') as file:
    file.write("Hello AI-ML Journey!\nWelcome to Day 6: File Handling.\n")

# Reading the whole file content
with open('sample.txt', 'r') as file:
    content = file.read()
    print("Full file content:")
    print(content)

# Reading line by line
with open('sample.txt', 'r') as file:
    print("Reading line by line:")
    for line in file:
        print(line.strip())  # strip() removes the newline character

# --- Writing to a file ---

# Appending new lines
with open('sample.txt', 'a') as file:
    file.write("Appending this new line.\n")

# Verifying append by reading again
with open('sample.txt', 'r') as file:
    print("\nAfter appending:")
    print(file.read())