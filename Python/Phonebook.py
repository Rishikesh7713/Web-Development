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


            

        
