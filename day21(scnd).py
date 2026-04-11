'''Largest Prime Factor Write a program to find the largest prime factor of a given number.'''


num = int(input("Enter a number: "))
largest = 0
for i in range(2, num + 1):
    if num % i == 0:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            largest = i
print("Largest Prime Factor:", largest)



'''Output
Enter a number: 28
Largest Prime Factor: 7'''