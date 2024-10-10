# set
#student_info = {12, 'john', 'john'}
# empty = set() # creating empty set

#print(student_info)

#numbers = {23, 3, 5, 90}
#numbers.add(10)

# update set
new_nums = {1, 4, 6}
#numbers.update(new_nums)

#print(numbers)

# removing elements from a set

#numbers.discard(90)

# iterate items in a set

#for number in numbers:
    # print(numbers)
    #pass
# find number of set of elements
#num = len(numbers)    

#print(num)

# set operations
# union of sets

setA = {1, 3, 5}
setB = {3, 5, 1}
uni = setA | setB
# intersection
#intersection = setA & setB
# difference between two sets

diff = setA - setB
# check if two sets are equal
if setA  == setB:
    print('setA and setB are equal')
else:
    print('the sets are not equal')
    
