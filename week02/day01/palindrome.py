import string

def is_palindrome(s):
    # Remove punctuation and convert to lowercase
    s = ''.join(char.lower() for char in s if char not in string.punctuation)
    # Remove spaces
    s = s.replace(" ", "")
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Get input from the user
input_string = input("Enter a string: ")

# Check if the input string is a palindrome
if is_palindrome(input_string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")