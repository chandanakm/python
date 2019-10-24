visitedlist=[]
duplicate=[]
unique=[]
inputfile=open(r'D:\Desktop\Python_assignments\Python_Assignment_1\data.txt','r')
data=inputfile.readlines()
print("INPUT DATA:\n",data)
print("\n")

'''-----------------------#unique and duplicate---------------------------------'''

outputfile=open(r'D:\Desktop\Python_assignments\Python_Assignment_1\uniq.txt','w')
outputfile1=open(r'D:\Desktop\Python_assignments\Python_Assignment_1\dup.txt','w')
for line in data:
    if line not in visitedlist:
         visitedlist.append(line)
    else:
        if line not in duplicate:
            outputfile1.write(line)
            duplicate.append(line)
print("visitedlist:\n",visitedlist)
print("\nduplicatelist:\n",duplicate)
for line in visitedlist:
    if ((line in visitedlist)&(line not in duplicate)):
        outputfile.write(line)
        unique.append(line)
print("\nunique:\n",unique)

outputfile.close()


'''-------------------#descending sort-------------------------------'''

newlist=[]
final=[]
outputfile2=open(r'D:\Desktop\Python_assignments\Python_Assignment_1\sort.txt','w')
#converting each element(string) in to list by deleting '#'
for line in visitedlist:
    splittedlist=line.split('#')
    newlist.append(splittedlist)#adding each list(newlist) in to one single list(nlist) 
print("\nCONVERTED LIST OF lists\n",newlist)
for i in range(1,len(newlist)):#descending order
    for j in range(i+1,len(newlist)):
        if(newlist[i][4]<newlist[j][4]):
            newlist[i],newlist[j]=newlist[j],newlist[i]
print("\nDESCENDING ORDER IN SALARIES:\n",newlist)#convert back all list in to string by adding '#' and append to new list listnew
for line in newlist:
    string='#'.join(line)
    final.append(string)
print("\nBACK TO STRING:",final)#add each line from list to outputfile
for line in final:
    outputfile2.write(line)
outputfile2.close()
    






    
