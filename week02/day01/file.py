# file = open('mbox.txt')

# count = 0

#
# for mistari in file:
    # count = count + 1
 # prompt= input("enter the file nam")
# print(f"line count: {count}")    

# for word in file:
   # if word.startswith('From'):
       # print(word)

#for word in file:

   # if word.startswith('From'):
        # print(word)
       # email = word.find('@')
       # after = word.find(' ', email)
       # host=word[email+1:after]
       # print(host)

# writting into a file
# file = open('sample.txt', 'w')
# text = 'samle txt'
#file.write(text)
#file.close()
# print(file)
# Function to count the number of words in a sentence

# Function to count the number of words in a sentence

# def count_words(sentence):
    # Split the sentence into words
  #  words = sentence.split()
    # Return the number of words
   # return len(words)

# Input sentence from the user
# sentence = input("enter a sentence: ")
 
# Count the words in the sentence
# word_count = count_words(sentence)

# Print the number of words
# print(f"The number of words in the sentence is: {word_count}")

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
