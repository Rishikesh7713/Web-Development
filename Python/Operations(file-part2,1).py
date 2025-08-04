with open('my_file.txt','w')as file:
    file.write("Hey, I am Penguin and I am 12 years old!")
file.close()

with open('my_file.txt','r')as file:
    data=file.readlines()
    for i in data:
        split=i.split()
        print(split)
file.close()