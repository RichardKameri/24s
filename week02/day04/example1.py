# Example1 find
import re
string = 'pilling'
pat = r'..g' # any character
match = re.search(pat, string)

if match:
    print(match.group())
    # output 'ing'
else:
    print('not found')