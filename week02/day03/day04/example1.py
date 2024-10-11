# Example1 find
import re
string = '123-456-7890'
pat = r'\d{3}-\d{3}-\d{4}'
match = re.search(pat, string)

if match:
    print(match.group())
    # 123
else:
    print('not found')