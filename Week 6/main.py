# try:
#     # Code that might raise an exception
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# result = 10 / 0
# print(result)


# try:
#     # Code that might raise an exception
#     result = int("not a number")
# except (ValueError, TypeError) as e:
#     print(f"An error occurred: {e}")

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# finally:
#     print("This will always execute.")

# try:
#     result = 10 / 2
# except ZeroDivisionError:
#     print("You can't divide by zero!")
# else:
#     print("No errors occurred!")

# age = -5
# if age < 0:
#     raise ValueError("Age can't be negative!")


# class NegativeNumberError(Exception):
#     pass


# def check_number(num):
#     if num < 0:
#         raise NegativeNumberError("Negative number is not allowed!")


# try:
#     check_number(-1)
# except NegativeNumberError as e:
#     print(e)

# file = open("text.txt", "r")
# try:
#     content = file.read()
# finally:
#     file.close()

with open("late.txt", "r") as file:
    content = file.read()
    print(content)

# with open("assets/text.txt", "r") as File1:
#     with open("assets/late.txt", "w") as File2:
#         for line in File1:
#             File2.write(line)
