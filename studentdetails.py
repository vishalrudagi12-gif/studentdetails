def calculate_average(m1, m2, m3):
    return (m1 + m2 + m3) / 3

def calculate_grade(avg):
    if avg >= 90:
        return "S"
    elif avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    else:
        return "F"

def display_details(name, department, semester, m1, m2, m3):
    average = calculate_average(m1, m2, m3)
    grade = calculate_grade(average)
    print("STUDENT GRADE CALCULATOR")
    print("Student Name: ", name)
    print("Department:", department)
    print("Semester:", semester)
    print("Subject 1 Marks:", m1)
    print("Subject 2 Marks:", m2)
    print("Subject 3 Marks:", m3)
    print("Average Marks:", round(average, 2))
    print("Grade:", grade)

def main():
    name = "Bhavana"
    department = "Computer Science"
    semester = 3
    m1 = 96
    m2 = 88
    m3 = 92
    display_details(name, department, semester, m1, m2, m3)

if __name__ == "__main__":
    main()