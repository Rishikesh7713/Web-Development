file=(open('my_file.txt','r'))
print(file.read())
file.close()

file=(open('my_file.txt','r'))
print("Read in Parts")
print(file.read(8))
file.close()

file=(open('my_file.txt','a'))
file.write("Hey I am Penguin!")
file.close()