
# Cognifyz Internship
# Level 1 - Task 1
# String Reversal

def reverse_string(text):

    reversed_text = text[::-1]

    return reversed_text


# Get input from user
user_text = input("Enter a word: ")

# Call the function
result = reverse_string(user_text)

# Display the result
print("Reversed string:", result)
