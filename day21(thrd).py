'''Sum of the series of n terms Write a program to calculate the sum of the series 1 + 1/2 + 1/3 + ... + 1/n up to the nth term.'''


n = int(input("Enter value of n: "))
sum_series = 0
for i in range(1, n + 1):
    sum_series += 1 / i
print("Sum of series:", sum_series)


'''Output
Enter value of n: 5
Sum of series: 2.283333333333333'''
