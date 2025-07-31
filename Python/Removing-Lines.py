file1=open('my_file.txt','r')
file2=open('file2.txt','w')
for line in file1.readlines():
    if not(line.startswith('h')):
       print(line)
       file2.write(line)
file1.close()
file2.close()

