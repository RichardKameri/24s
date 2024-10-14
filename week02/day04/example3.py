#  examlple3
import re
string = 'piigiii'
pat = r'pi+'
match = re.search(pat, string)
if match:
    print(match.group())
else:
    print('not found')