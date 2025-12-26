import math
n=int(input("Enter a Number : "))
def bit():
    if n==0:
        return 0
    res=n & (~n + 1)
    return int(math.log2(res))+1

if __name__==" __main__ ":
    n=18
    print(bit(n))