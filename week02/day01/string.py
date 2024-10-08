# text = "mango is sweet"
# print(text.capitalize())
# print(text[-1])
# print(len(text))
# print(text[6:-2])

# count = 0

# for letter in text:
#    if letter == 'e':
 #       count = count + 1
#print(count)        

# check = 'h' in text
# print(check)

#if text == 'banana':
   # print("yes,itis a banana")

# if text < 'banana':
   # print('your word, + text =', 'come before banana')
# elif text > "banana":
   # print(f"your word, {text},comes after banana")
# else:
    # print("all are banana")


# text = "mango is sweet"

# Split the string into words
# words = text.split()

# Convert the word "sweet" to uppercase
# words[2] = words[2].upper()

# Join the words back into a single string
# result = " ".join(words)

# print(result)

word = 'my email address is richardkameri327@gmail.com and is verified'

email = word.find('@')
after = word.find('', email)
host=word[email+1:]
print(host)
