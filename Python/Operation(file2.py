file=(open('my_file.txt','r'))
print("Reading first Line")
print(file.readline())
file.close

file=(open('my_file.txt','r'))
print("Reading three Line")
print(file.readline())
print(file.readline())
print(file.readline())
file.close

file=(open('my_file.txt','r'))
print("Reading All Lines")
for i in file:
    print(i)
file.close

