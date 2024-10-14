# matches the start of a string
import re
string = 'foobar'
pat = r'b\w+'
match = re.search(pat, string)
if match:
    print(match.group())
    # output 1 2 3
else:
    print('not found')    