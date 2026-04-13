'''Finding the Most Frequent Element in an Array
Write a program to find the most frequent element in an array.
'''
arr = list(map(int, input("Enter numbers: ").split()))
max_count = 0
result = arr[0]
for i in arr:
    count = arr.count(i)
    if count > max_count:
        max_count = count
        result = i
print("Most frequent element:", result)

'''Output
Enter numbers: 1 2 3 2 4 2
Most frequent element: 2
'''