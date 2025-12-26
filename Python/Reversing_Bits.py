def reverse_bits(n):
    result = 0
    for i in range(32):
        result = (result << 1) + (n & 1)
        n >>= 1
    return result
n=int(input("Enter a Number : "))
print("Input : ",n)
print("Reversed Integer : ",reverse_bits(n))