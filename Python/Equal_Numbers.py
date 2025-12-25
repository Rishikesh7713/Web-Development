no1=int(input("Enter Number 1 : "))
no2=int(input("Enter Number 2 : "))
def equal_or_not(no1,no2):
    if((no1^no2)==0):
        print("Numbers are Equal")
    else:
        print("Numbers are Not Equal")
equal_or_not(no1,no2)