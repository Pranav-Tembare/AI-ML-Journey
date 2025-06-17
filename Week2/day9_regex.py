# day9_regex.py

import re

print("\n--- re.search() ---")
text = "My email is example@mail.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)
if match:
    print("Found:", match.group())

print("\n--- re.findall() ---")
text = "Emails: test1@gmail.com, test2@yahoo.com"
emails = re.findall(r"\w+@\w+\.\w+", text)
print("All emails found:", emails)

print("\n--- re.sub() ---")
text = "Visit my site at http://example.com"
new_text = re.sub(r"http\S+", "[LINK]", text)
print(new_text)

print("\n--- Common Patterns Examples ---")
sample = "ID123 name:John age:25"
digits = re.findall(r"\d+", sample)
words = re.findall(r"\w+", sample)
print("Digits:", digits)
print("Words:", words)

# --- Mini Challenges ---

print("\n--- Challenge 1: Extract phone numbers ---")
text = "Call me at 9876543210 or 9123456789"
numbers = re.findall(r"\d{10}", text)
print("Phone numbers found:", numbers)

print("\n--- Challenge 2: Find hashtags ---")
post = "Loving this! #python #AI #ML"
hashtags = re.findall(r"#\w+", post)
print("Hashtags:", hashtags)

print("\n--- Challenge 3: Censor bad words ---")
text = "You are so dumb and stupid!"
clean = re.sub(r"dumb|stupid", "[censored]", text)
print("Cleaned text:", clean)
