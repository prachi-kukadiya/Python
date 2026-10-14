students=[
    {"id": 1, "name":"Alice", "marks":85},
    {"id": 2, "name":"Bob", "marks":78},
    {"id": 3, "name":"Jack", "marks":87},
    {"id": 4, "name":"David", "marks":98},
    {"id": 5, "name":"Ray", "marks":68},
]

student_id = int(input("Enter student ID :"))
name = input("Enter student name :")
marks = int(input("Enter student marks :"))

new_student = {
    "id": student_id,
    "name": name,
    "marks": marks
} 

students.append(new_student)

print("Updated Students List:")

for student in students:
    print(student)