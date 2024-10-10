def are_anagrams(str1, str2):
    # Convert both strings to lowercase to make the check case-insensitive
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Check if the lengths of the strings are the same
    if len(str1) != len(str2):
        return False
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

# Example usage
string1 = "Listen"
string2 = "Silent"

if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')
