'''fvar=open(r'D:\Desktop\sample.txt','r')
data=fvar.readlines()
fvar.close()
print(data)
print(type(data))


fvar=open(r'D:\Desktop\samplewrite.txt','w')
data="this is a sample write file"
fvar.write(data)
print("complete")
fvar.close() #read() allows to read in string mode
#readlines- list mode
#write- to write string
#writelines to write list


fvar=open(r'D:\Desktop\samplewrite.txt','w')
l1=['python\n','java\n','c\n']
fvar.writelines(l1)
print("complete")
fvar.close()#write mode will erase old data from file
'''

fvar=open(r'D:\Desktop\samplewrite.txt','a')
l1=['python\n','java\n','c\n']
fvar.writelines(l1)
print("complete")
fvar.close()#append mode will not erase the old data present in the file with new one
