file_read=open('my_file.txt','r')
print("File in Read mode")
print(file_read.read())
file_read.close()

file_write=open('my_file.txt','w')
print("File in Write mode")
file_write.write("Hello Guys! My name is Rob and I am studying in Class 7")
file_write.close()

file_append=open('my_file.txt','a')
print("File in Write mode")
file_append.write("Hello Guys! My name is Lob and I am studying in Class 5")
file_append.close()