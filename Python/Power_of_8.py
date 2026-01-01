def powerof8 (n):
    if n <= 0:
        return False
    mask=0x49249249
    if (n & mask) != 0:
        return True
    else:
        return False
    
num=int(input("Enter a Number : "))
if powerof8(num):
    print(num, " is a Power of 8")
else:
    print(num, " is NOT a Power of 8")