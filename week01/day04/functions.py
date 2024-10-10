def get_person_info():
    name = "Alice"
    age = 30
    return name, age

# Calling the function and unpacking the returned values
name, age = get_person_info()
print(f"Name: {name}, Age: {age}")