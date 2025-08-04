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

