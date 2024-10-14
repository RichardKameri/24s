# example 5 finding email
import re
string = 'purple alice-b@google.com monkey dishwasher'
pat = r'[\w.-]+@[\w.-]+' # any character
match = re.search(pat, string)

if match:
    print(match.group())
    # output: alice-b@google.com
else:
    print('not found')