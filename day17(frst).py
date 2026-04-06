'''Binary to decimal and decimal to binary conversion functions.'''


def binary_to_decimal(binary_str):
    decimal = 0
    position = 0
    for i in range(len(binary_str) - 1, -1, -1):
        bit = int(binary_str[i])
        decimal += bit * (2 ** position)
        position += 1
    return decimal
def decimal_to_binary(n):
    if n == 0:
        return "0"
    remainders = []
    while n > 0:
        remainders.append(str(n % 2))
        n = n // 2
    return "".join(reversed(remainders))
b = input("Enter a binary number: ")
print("Decimal equivalent:", binary_to_decimal(b))
d = int(input("Enter a decimal number: "))
print("Binary equivalent:", decimal_to_binary(d))



'''output:
Enter a binary number: 1010
Decimal equivalent: 10
Enter a decimal number: 17
Binary equivalent: 10001'''
