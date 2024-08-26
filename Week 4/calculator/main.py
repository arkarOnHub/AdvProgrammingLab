from utilities.calculator import (
    add as add_def,
    subtract as subtract_def,
    multiply as multiply_def,
    divide as divide_def,
)
from utilities.string_operations import (
    reverse_string,
    capitalize_string,
    lowercase_string,
    uppercase_string,
)


a = int(input("No 1 : "))
b = int(input("No 2 : "))

print("Using calculator.py:")
print("Addition:", add_def(a, b))
print("Subtraction:", subtract_def(a, b))
print("Multiplication:", multiply_def(a, b))
print("Division:", divide_def(a, b))


sample_string = input("The Input String : ")
print("\nUsing string_operations.py:")
print("Original:", sample_string)
print("Reversed:", reverse_string(sample_string))
print("Capitalized:", capitalize_string(sample_string))
print("Lowercase:", lowercase_string(sample_string))
print("Uppercase:", uppercase_string(sample_string))
