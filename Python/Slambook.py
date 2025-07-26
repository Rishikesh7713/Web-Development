import sys
def slambook():
  rows ,cols=int(input("Enter ab= Number")), 3
  text_slambook=[]
  print(text_slambook)
  
  for i in range(rows):
   print("Enter Name, Class & Address")
   temp=[]

   for j in range(cols):
    if j==0:
     temp.append(str(input("Enter your Name")))
    if j==2:
     temp.append(int(input("Enter your class")))
    if j==3:
     temp.append(str(input("Enter your Address")))
    text_slambook.append(temp)
    print(text_slambook)
   return text_slambook
def menu():
 print("Now you can countinue here")
 print("1. Add a Name")
 print("2. Remove a name")
 print("3. Search")
 print("4. Display") 
 print("5. Exit")
 choice=int(input("Enter your Choice"))
 return choice
def add_con(sb):
 dip=[]
 for i in range(len(sb[0])):
  if i==0:
   dip.append(str(input("Enter your Name: ")))
   
  if i==1:
   dip.append(str(input("Enter your Class: ")))

  if i==2:
   dip.append(str(input("Enter your Address: ")))
def rem_existing():
 query=str(input("Enter the Name to be Searched"))
 temp=0

 for i in range(len(sb)):
  if query==sb[i][0]:
   temp+=1
   sb.pop(i)
   print("Done")
   return sb
  
  if temp==0:
   print("Sorry!It is Invalid")
 return sb
  
def del_all():
 return pb.clear()

print("..................................................................")
print("Welcome to the Slambook")
print("Now you may Proceed")
print("..................................................................")

ch=1
sb=slambook
while ch in(1, 2, 3, 4, 5):
 ch=menu()
 if ch==1:
  pb=add_con(sb)
 elif ch==2:
  pb=rem_existing(sb)
 elif ch==3:
  pb=del_all(sb)


