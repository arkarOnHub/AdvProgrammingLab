# num = [1, 2, 4, 5, 6]

# test = list(map(lambda x: x * 2, num))

# print(test)


students = [
    {"name": "Jim", "grade": 99},
    {"name": "Tim", "grade": 49},
    {"name": "Bim", "grade": 29},
]

sorted_students = sorted(students, key=lambda student: student["grade"], reverse=True)

print(sorted_students)
