import math;
def printallsubSet(set,SetSize):
    powerSubSetSize= (int) (math.pow(2, SetSize))
    outer=0
    inner=0

    for outer in range(0, powerSubSetSize):
        for inner in range(0, SetSize):
            if((outer & (1 << inner))>0):
                print(set[inner], end= "")
        print("")

size=int(input("Enter Array Size : "))
set=[]
for i in range(0, size):
    n=str(input("Enter Element : "))
    set.append(n)
printallsubSet(set, len(set))