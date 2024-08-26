numbers = [1, 2, 3, 4, 5]
modified_numbers = [x + 10 if x % 2 == 0 else x - 1 for x in numbers]
print(modified_numbers)
