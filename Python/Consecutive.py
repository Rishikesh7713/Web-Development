def max_consecutive_ones(n):
    count = 0
    while n != 0:
        n = (n & (n << 1))
        count += 1
    return count
n=int(input("Enter a Number : "))
print("The number is: ",n)
print("Binary representation: ",bin(n))
print("Length of longest consecutive 1s: ",max_consecutive_ones(n)) 