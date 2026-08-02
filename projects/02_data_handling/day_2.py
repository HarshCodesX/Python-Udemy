"""
 Challenge: Student Marks Analyzer

Create a Python program that allows a user to input student names along with their marks and then calculates useful statistics.

Your program should:
1. Let the user input multiple students with their marks (name + integer score).
2. After input is complete, display:
   - Average marks
   - Highest marks and student(s) who scored it
   - Lowest marks and student(s) who scored it
   - Total number of students

Bonus:
- Allow the user to enter all data first, then view the report
- Format output clearly in a report-style layout
- Prevent duplicate student names
"""

def collect_student_data():
    students = {}
    while True:
        name = input("Enter the student name: ").strip()

        if name.lower() == "done":
            break
        if name in students:
            print("Student already exists")
            continue

        try:
            marks = float(input(f"Enter marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("Please enter a valid number for marks")
            
    return students

def display_report(students):
    if not students:
        print("No student data!")
        return
    marks = list(students.values())
    max_score = max(marks)
    min_score = min(marks)
    average = sum(marks) / len(marks)

    topper = [name for name, score in students.items() if score == max_score]
    bottom = [name for name, score in students.items() if score == min_score]

    print("\nStudents marks report")

    print("-" * 30)

    print(f"Total number of students: {len(students)}")
    print(f"Average marks of students: {average:.2f}")
    print(f"Highest marks among students: {max_score} and scored by {topper}")
    print(f"Lowest marks among students: {min_score} and scored by {bottom}")

    print("-" * 30)
    print("Detailed marks")
    for name, score in students.items():
        print(f"{name} - {score}")

data = collect_student_data()
display_report(data)