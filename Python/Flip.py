def totalFlips(no1, no2):
    flips=0
    while(no1 > 0 or no2 > 0):
        t1=(no1 & 1)
        t2=(no2 & 1)
        if(t1 != t2):
            flips+=1
        no1>>=1
        no2>>=1
    return flips
no1=int(input("Enter First Number : "))
no2=int(input("Enter Second Number : "))
print("\nNumber of Flips Needed : ",totalFlips(no1, no2))