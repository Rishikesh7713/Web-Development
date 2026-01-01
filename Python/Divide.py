def  divide(ourDividend, ourDivisor):
     sign=(-1 if((ourDividend<0) ^ (ourDivisor<0)) else 1)
     ourDividend=abs(ourDividend)
     ourDivisor=abs(ourDivisor)
     quotientno=0
     tempno=0
     for i in range(31, -1, -1):
          if (tempno + (ourDivisor<<i)<=ourDividend):
               tempno+=ourDivisor<<i
               quotientno |=1<<i
     if sign==-1:
        quotientno=-quotientno
     return quotientno

a=int(input("Enter a for a/b : "))
b=int(input("Enter b for a/b : "))
print("Result of ",a,(" / ",b," = ",divide(a,b)))