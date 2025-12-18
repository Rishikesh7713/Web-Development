def setOrNot(number,n):
    if number & (1<<(n-1)):
        print("\nSet")
    else:
        print("\nNot Set")
number=int(input("Enter a Number : "))
n=int(input("Enter a Bit Number : "))
setOrNot(number,n)
