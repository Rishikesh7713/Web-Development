newfile=open('newfile2.txt','x')
newfile.close()

import os
print("Checking if the file exists or not.......")
if os.path.exists('my_file.txt'):
    os.remove('my_file.txt')
else:
    print("This file does not Exists")
    
    file2=open('my_file.txt','w')
    file2.write("Hey I am Panda and I am 5 years old")

with open('my_file.txt','w')as file:
    file.write("Hey, I am Penguin and I am 9 years old!")
file.close()

with open('my_file.txt','r')as file:
    data=file.readlines()
    for i in data:
        split=i.split()
        print(split)
file.close()