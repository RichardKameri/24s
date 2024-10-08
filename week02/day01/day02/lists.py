[10,20,30,40] #integers
['moses','ruth','richard'] # various data types
['amos', 12, 40.5, ['oranges','mangoes']] # various data types
[] # empty list

students = ['richard','ruth','moses', 'amos', 'ezekiel']
numbers = [10, 11, 12]
empty = [23, 14, 6]

# print(students, numbers, empty)
#print(students[0])

# sum = numbers * 4 
# print(sum)


# slicing operations
# print(students[2:4])
#students[3:5] = ['jesee', 'cyril']
#print(students)

# lists methods
# append
t = [1, 2, 3]
# extend
r = [12, 13, 14]
t.extend(r)
# sort
t.sort()


# deleting elements
my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# my_list.pop(2)
# del my_list[1]
# my_list.remove('d')
# del my_list[1:6]
#print(my_list)


# lists functions
#list = [3, 41, 12, 9, 74, 15]
#rint(len(my_list))
#print(max(my_list))
#print(min(list))
#print(sum(list))
#print(sum(list)/len(list))

# challenge
total = 0
count = 0

while (True):
    prompt = input('enter a number: ')
    if prompt == 'done':
        break
value = int(prompt)
total = total + value
count = count + 1

average = total / count
print(f'average: {average}')

# modify code to print: sum, length