file_read=open('my_file.txt','r')
print("File in Read mode")
print(file_read.read())
file_read.close()

file_write=open('my_file.txt','w')
print("File in Write mode")
file_write.write("Hello This is me This is for codingal This is File After Classproject")
file_write.close()

file_append=open('my_file.txt','a')
print("File in Write mode")
file_append.write("Hello This is me This is for codingal This is File After Class project of Date: 26/07/2025")
file_append.close()