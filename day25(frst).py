'''Find the Frequency of Each Element in an Array
Calculate the frequency of each element in the array.
'''

arr = list(map(int, input("Enter elements: ").split()))
freq = {}
for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)


'''Output
Enter elements: 1 2 2 3 3 3
{1: 1, 2: 2, 3: 3}'''