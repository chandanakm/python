'''n=int(input("enter the range for fibonacci series:\n"))
f1=0
f2=1
print(f1)
print(f2)
while(n-2):
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3)
    n=n-1'''

import math
str="python classes"
res=len(str)
print(res)
mid=int(res/2)
print("midpoint:",int(mid))
fh=str[0:mid]
sh=str[mid:]
fh[::-1]
sh[::-1]
f=fh[::-1]+" "+sh[::-1]
print(f)
