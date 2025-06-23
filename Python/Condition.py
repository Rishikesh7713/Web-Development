num=int(input("Enter a Number"))
if(num>0):
 print(num," is a positive number")
elif(num<0):
 print(num," is a negative number")
else:
 print(num," is zero")


if num%2==0:
 print(num," is Even")
else:
 print(num," is Odd")


 l=["Mango", "apple", "kiwi", "orange"]
 print("Length of list:", len(l))
 print("First element", l[0])
 print("Last element", l[-1])

 l.append("papaya")
print("Updated list :", l)

l.remove ("kiwi")
print("Updated list :", l)

l.sort()
print("Sorted list :", l)

l.pop(1)
print("Popped list", l)

l.reverse()
print("Reversed list :", l)

print("Multiplication in list", list*2)

list = list[:4]
print("Sliced list", l)

list.clear