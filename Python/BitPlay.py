def noOfBits(n):
    ones=0
    zeros=0
    while n>0:
        if (n&1==1):
            ones+=1
        else:
            zeros+=1
        n>>=1
    print("No of Ones :",ones,"\n")
    print("No of Zeros :",zeros)

n=int(input("Enter a Number : "))
noOfBits(n)