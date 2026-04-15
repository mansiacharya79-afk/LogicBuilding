'''Find the Second Largest Element in an Array
Find the second largest element in the array.
'''

arr=list(map(int, input("Enter the array elements:").split()))
arr=list(set(arr))
if len(arr)<2:
    print("There is no second largest array element")
else:
    arr.sort()
    print("The second largest array element is :",arr[-2])


'''Output:
Enter the array elements: 6 7 5 2 9
The second largest array element is : 7
'''