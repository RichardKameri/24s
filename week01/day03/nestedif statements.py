# Function to determine the grade
def determine_grade(score):
    if score >= 90:
        if score >= 95:
            return "A+"
        else:
            return "A"
    elif score >= 80:
        if score >= 85:
            return "B+"
        else:
            return "B"
    elif score >= 70:
        if score >= 75:
            return "C+"
        else:
            return "C"
    elif score >= 60:
        if score >= 65:
            return "D+"
        else:
            return "D"
    else:
        return "F"

# Main program
score = int(input("Enter the student's score: "))
grade = determine_grade(score)
print(f"The grade for a score of {score} is: {grade}")
