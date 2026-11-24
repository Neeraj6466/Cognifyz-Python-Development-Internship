
# Cognifyz Internship
# Level 2 - Task 5
# File Manipulation - Word Counter

from pathlib import Path
import string

# Get text file path
file_path = Path(__file__).with_name("sample.txt")

# Read the file
with open(file_path, "r") as file:
    content = file.read()

# Convert text to lowercase
content = content.lower()

# Remove punctuation
for symbol in string.punctuation:
    content = content.replace(symbol, "")

# Split text into words
words = content.split()

# Count each word
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display words in alphabetical order
print("===== WORD COUNT =====")

for word in sorted(word_count):
    print(word, ":", word_count[word])
