
# Cognifyz Internship
# Level 1 - Task 5
# Palindrome Checker

def check_palindrome(text):

    reversed_text = text[::-1]

    if text == reversed_text:
        return True
    else:
        return False


# Get input from user
user_text = input("Enter a word: ")

# Check palindrome
if check_palindrome(user_text):
    print("It is a Palindrome!")
else:
    print("It is NOT a Palindrome!")
