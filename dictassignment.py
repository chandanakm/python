l1=['a','b','c','d','e','f']
l2=[20,60,80]
d1={}
for keys in l1:
    for values in l2:
        d1[keys]=values;
        l2.remove(values)
        break
    else:
        d1[keys]="nan"
print(d1)
