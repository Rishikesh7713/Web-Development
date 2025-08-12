class quiz:
    qn=0
    var=0
    ans1=""
    ans2=""
    ans3=""
    ans4=""
    ans5=""
    for i in range(0,6):

         if i==1:
            print("Which planet is known as the “Red Planet”?")
            ans1=input("Enter the Answer")
            if ans1=="mars".lower():
                print("Yes it is the answer")
                var+=1
            else:
                var=var
         if i==2:
            print("What is the currency of Japan?")
            ans2=input("Enter the Answer")
            if ans2=="japanese yen".lower():
                print("Yes it is the answer")
                var+=1
            else:
                var=var
         if i==3:
            print("What is the most widely spoken language in the world?")
            ans3=input("Enter the Answer")
            if ans3=="mandarin chinese".lower():
                print("Yes it is the answer")
                var+=1
            else:
                var=var       
         if i==4:
            print("What comes once in a minute, twice in a moment, but never in a thousand years?")
            ans4=input("Enter the Answer")
            if ans4=="The letter 'M'".lower():
                print("Yes it is the answer")
                var+=1
            else:
                var=var
         if i==5:
            print("What has a thumb and four fingers but is not a hand?")
            ans5=input("Enter the Answer")
            if ans5=="glove".lower():
                print("Yes it is the answer")
                var+=1
            else:
                var=var        
    print("Your marks are ",var,"out of 5")

            