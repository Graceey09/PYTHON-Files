# Step 1: Create a nested list with student names and grades
students = []
n = int(input("Enter the number of students: "))

for _ in range(n):
    name = input("Enter student name: ")
    grade = float(input("Enter student grade: "))
    students.append([name, grade])

# Step 2: Find the second lowest grade
grades = set([student[1] for student in students])
sorted_grades = sorted(grades)
second_lowest_grade = sorted_grades[1]

# Step 3: Create a list of students with the second lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# Step 4: Sort the list of students alphabetically
second_lowest_students.sort()

# Step 5: Print each student's name on a new line
print("Students with the second lowest grade:")
for student in second_lowest_students:
    print(student)
