'''Print the Array in Sorted Order (Ascending and Descending):
Write a program to sort an array in ascending and descending order. For example:
'''

arr = list(map(int, input("Enter numbers: ").split()))
ascending = sorted(arr)
descending = sorted(arr, reverse=True)
print("Ascending:", ascending)
print("Descending:", descending)


'''Output
Enter numbers: 5 2 9 1 5
Ascending: [1, 2, 5, 5, 9]
Descending: [9, 5, 5, 2, 1]'''