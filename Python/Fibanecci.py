def fib(nterms):
    n1,n2=0,1
    count=0
    while count<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count+=1
    nterms=int(input("How many Terms"))   
    if nterms <=0:
        print("PLease Enter an positive no")
    elif nterms==1:
        print("Fibonacci sequance upto ",nterms,":")
        fib(nterms)
    else:
        print("Fibonacci sequance")
        fib(nterms)