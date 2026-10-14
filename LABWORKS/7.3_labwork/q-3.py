students=[
    {"id": 1, "name":"Alice", "marks":85},
    {"id": 2, "name":"Bob", "marks":78},
    {"id": 3, "name":"Jack", "marks":87},
    {"id": 4, "name":"David", "marks":98},
    {"id": 5, "name":"Ray", "marks":68},
]

student_id = int(input("Enter student ID to search student :"))
found = False
for student in students:
    if student["id"]==student_id:
        print("Student Details :-")
        print("ID :",student["id"])
        print("Name :",student["name"])
        print("Marks :",student["marks"])
        found = True
        break

if not found:
    print("Student not found.")
