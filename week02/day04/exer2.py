import re

def validate_password(password):
    # Check for minimum length of 8 characters
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        return "Password must contain at least one digit."

    # Check for at least one special character
    if not re.search(r"[@$!%*?&]", password):
        return "Password must contain at least one special character (@$!%*?&)."

    return "Password is valid."

# Input from the user
password = input("Enter your password: ")

# Validate the password
validation_result = validate_password(password)
print(validation_result)