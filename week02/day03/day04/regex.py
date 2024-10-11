import re

string = 'Hello world'
pattern = r'^H' # make a pattern to search a word that starts with 'h'
match = re.search(pattern, string)
if match:
    print('found', match.group())
else:
    print('did not find')


