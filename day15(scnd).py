'''Print Prime Numbers Within a Range:
Write a program to display all prime numbers between two intervals entered by the user'''


num1 , num2 = map(int,input("Enter two number :").split())
primes = []
for num in range(num1, num2 + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)
print("Prime numbers between", num1, "and", num2, ":", ", ".join(map(str, primes)))




'''output:
Enter two number :10 20
Prime numbers between 10 and 20 : 11, 13, 17, 19
'''
