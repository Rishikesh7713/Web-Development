import numpy as np
a=np.arange(9,dtype=np.float64).reshape(3,3)
print("First Operation :")
print(a)
print("\n")

b=np.array([7,7,7])
b1=np.array([6,5,4])
rb=np.add(b,b1)
print("Second Operation ; Add: ")
print(rb)
print("\n")

c=np.array([7,7,7])
c1=np.array([6,5,4])
rc=np.subtract(c,c1)
print("Third Operation ; Subtract :")
print(rc)
print("\n")


d=np.array([7,7,7])
d1=np.array([6,5,4])
rd=np.multiply(d,d1)
print("Fourth Operation ; Multiply :")
print(d)
print("\n")