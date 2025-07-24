import sys

def initial_phonebook():
    rows,cols=int(input("Enter a Number")), 5
    phone_book=[]
    print(phone_book)

    for i in range(rows):
        print("Enter Contact, Name and other details")
        print("NOTE* Indicates mandetory field")
        temp=[]

        for j in range(cols):
            if j==0:
                temp.append(str(input("Enter name: ")))
                if temp[j]==''or temp[j]==' ':
                    sys.exit("Name is mandetory field, cause not filled exiting the process")

            if j==1:
                temp.append(int(input("Enter a Number: ")))

            if j==2:
                temp.append(str(input("Enter Email address: ")))
                if temp[j]==''or temp[j]==' ':
                    temp=None

            if j==3:
                    temp.append(str(input("ENner Date of Birth (dd/mm/yy)")))
                    if temp[j]==''or temp[j]==' ':
                     temp=None
                    
            if j==4:
                 temp.append(str(input("Enter Category (Family, Work, Friends, Others)")))
                 if temp[j]==''or temp[j]==' ':
                    temp=None

            phone_book.append(temp)
            print(phone_book)
        return phone_book
def menu():
    print("Now you can do it on this Phonebook")
    print("1. Add an Existing Contact")
    print("2. Remove an Existing Contact")
    print("3. Delete all Contact")
    print("4. Search for a Contact")
    print("5. Display all Contacts")
    print("6. Exit Phonebook")
    choice=int(input("Enter your choice"))
    return choice
def add_con(pb):
        dip=[]
        for i in range(len(pb[0])):
            if i==0:
                 dip.append(str(input("Enter your Name: ")))

            if i==1:
                dip.append(int(input("Enter your Number: ")))
            if i==2:
                 dip.append(str(input("Enter your Email address: ")))

            if i==3:
                dip.append(str(input("Enter your Date of Birth: ")))
                     
            if i==3:
             dip.append(str(input("Enter your Date of Birth: ")))
             pb.append(dip)
        return pb
               
def rem_existing():
            query=str(input("Enter the Name of Contact to be Searched"))
            temp=0
            for i in range(len(pb)):
                if query == pb[i] [0]:
                    temp+=1
                    pb.pop(i)
                    print("Query has been removed")
                    return pb
                     
                if temp==0:
                    print("Sorry! you have entered invalid Query")
            return pb
                     
def delete_all():
        return pb.clear()

def thanks():
     print("*****************************************")
     print("Thanks for using Slambook")
     print("Pls visit again")
     print("*****************************************")

print("............................................................................................")
print("Hello dear User! Welcome to the Phonebook")
print("Now you may Proceed")
print("............................................................................................")

ch=1
pb=initial_phonebook
while ch in(1, 2, 3, 4, 5):
    ch=menu()
    if ch==1:
        pb=add_con(pb)
    elif ch==2:
         pb=rem_existing(pb)
    elif ch==3:
         pb=delete_all(pb)
    else:
         thanks()