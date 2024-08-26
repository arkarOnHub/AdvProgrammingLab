students = [
    {"name": "Alice", "age": 20, "grade": 85, "major": "Physics"},
    {"name": "Bob", "age": 22, "grade": 90, "major": "Chemistry"},
    {"name": "Charlie", "age": 19, "grade": 78, "major": "Mathematics"},
    {"name": "Diana", "age": 21, "grade": 92, "major": "Biology"},
]

for items in students:
    if items["name"] == "Alice":
        items["grade"] = 87

    if items["name"] == "Diana":
        items["major"] = "Programming"

    print(items)
