# Create the dictionary with departments as keys and nested dictionaries as values
company_departments = {
    "HR": {
        "Alice": "HR Manager",
        "Bob": "Recruiter"
    },
    "IT": {
        "Charlie": "System Administrator",
        "David": "Software Developer"
    },
    "Sales": {
        "Eve": "Sales Manager",
        "Frank": "Sales Representative"
    }
}

# Display the dictionary
for department, employees in company_departments.items():
    print(f"\nDepartment: {department}")
    for name, role in employees.items():
        print(f"Name: {name}, Role: {role}")
