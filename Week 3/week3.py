# sqr = [x**2 for x in range(1, 10)]
# print(sqr)

num = ["even" if x % 2 == 0 else "odd" for x in range(1, 11)]
print(num)

# number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even_num = [n for n in number if n % 2 == 0]
# print(even_num)

# for i in range(20, 1):
#     print(i)

# i = 0

# while i < 10:
#     i += 1
#     if i % 2 == 0:
#         continue
#     print(i)


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


primes = [num for num in range(2, 101) if is_prime(num)]

result = sum(primes)

print("The sum of prime numbers between 1 and 100 is:", result)
