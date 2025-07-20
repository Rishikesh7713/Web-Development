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

 

