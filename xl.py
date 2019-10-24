from openpyxl import Workbook
myexcel=Workbook()
mysheet=myexcel.active
mysheet['A1']="name"
mysheet['B1']="age"
mysheet['C1']="salary"

n=['A','B','C','D','E','F']
a=[23,26,27,24,23,28]
s=[200,900,600,100,700,800]
startpos=2
rows=len(n)
i=0
while(rows>0):
    namestr='A'+str(startpos)
    agestr='B'+str(startpos)
    salstr='C'+str(startpos)
    mysheet[namestr]=n[i]
    mysheet[agestr]=a[i]
    mysheet[salstr]=s[i]
    rows-=1
    startpos+=1
    i+=1
    myexcel.save(r'D:/Desktop/test.xlsx')
