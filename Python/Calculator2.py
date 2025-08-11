
sign=input("Enter the sign. Do not type in letters or Numbers!")
no1=int(input("Enter no 1"))
no2=int(input("Enter no 2"))
ans=0
def signno():
    if sign=="+":
        ans=no1+no2
        print(ans)
    elif sign=="-":
        ans=no1-no2
        print(ans)
    elif sign=="x" or sign=="*":
        ans=no1*no2
        print(ans)
    elif sign=="/":
        ans=no1+no2
        print(ans)
signno.close()
     