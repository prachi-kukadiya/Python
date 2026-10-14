students=[
    {"id": 1, "name":"Alice", "marks":85},
    {"id": 2, "name":"Bob", "marks":78},
    {"id": 3, "name":"Jack", "marks":87},
    {"id": 4, "name":"David", "marks":98},
    {"id": 5, "name":"Ray", "marks":68},
]

print("Students who scored more than 80 marks:")

for student in students:
    if student["marks"]>80:
        print(student)