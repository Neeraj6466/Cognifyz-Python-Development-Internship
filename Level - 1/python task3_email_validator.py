
# Cognifyz Internship
# Level 1 - Task 3
# Email Validator

def validate_email(email):

    if "@" not in email:
        return False

    if email.count("@") != 1:
        return False

    username, domain = email.split("@")

    if username == "" or domain == "":
        return False

    if "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


# Get email from user
user_email = input("Enter your email address: ")

# Validate email
if validate_email(user_email):
    print("Valid Email Address")
else:
    print("Invalid Email Address")
