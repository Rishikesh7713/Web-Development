ofile=open('file2','w')
efile=open('my_file.txt','r')

linessofar=set()
for i in efile:
    print("Eliminating duplicate lines........")
    if i not in linessofar :
        ofile.write(i)
        linessofar.add(i)
ofile.close()
efile.close()