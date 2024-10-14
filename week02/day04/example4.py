# zero or more white spaces
import re
string = 'xx1 2 3xx'
pat = r'\d\s*\d\s*\d'
match = re.search(pat, string)
if match:
    print(match.group())
    # output 1 2 3
else:
    print('not found')    