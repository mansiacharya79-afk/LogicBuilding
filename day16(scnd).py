'''Check if an Integer Can Be Expressed as the Sum of Two Prime Numbers:
Write a program to check if a number can be expressed as the sum of two prime numbers. Print all such combinations'''


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
found = False
for i in range(2, num):
    j = num - i
    if is_prime(i) and is_prime(j):
        print(f"{num} = {i} + {j}")
        found = True
if not found:
    print(f"{num} cannot be expressed as the sum of two prime numbers")


'''output:
Enter a number: 10
10 = 3 + 7'''

