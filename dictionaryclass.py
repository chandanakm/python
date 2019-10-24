d1={'name':'ckm', 'place': 'hobby':'singing', 'pincode':560040}
print(d1['name'])
print(d1['place'])
print(d1['hobby'])
print(d1['pincode'])
d2={'name':'mkm', 'place':'bengaluru', 'hobby':'painting', 'pincode':560040}
#d3=d1+d2
#print(d3)
#d4=d1*3
#print(d4)
res= 'name' in d1
print(res)
res1='lastname' not in d2
print(res)
res2='place' not in d2
print(res2)# in and not in operator will work only for keys and not for values

'''functions on dictionary
len(), max(), min(), type(), d1.keys(), d1.values(), d1.items()'''

res3=len(d1)
print(res3)
res4=type(d1)#type(d1)__name__ : if u dont want word 'class' in output use this.
print(res4)
res5=max(d1)#max and min values work only for keys and not for values
print(res5)
res6=min(d1)
print(res6)
res7=d2.keys()
print(res7)
res8=d2.values()
print(res8)
res9=d2.items()
print(res9)
for x in d1:#it will print only keys
    print(x)
for x,y in d1.items():
    print(x,y)#to print both keys and values
#to fetch keys given values
for x,y in d1.items():
    if(y=='ckm'):
        print(x)
        
del d1['name'] # deletes first key value pair
print(d1)
'''d1.clear()#it will clear all entries in the dictionary
print(d1)

del d1
print(d1)# it will delete the dictionary variable only

d2.pop('name')
print(d2)#used to delete key value pair
'''
res=d1.get('x',3000)# when we ask value for key which is not in dict then it will print default value
print(res)
print(d1)
res=d1.setdefault('place',3000)#it will insert one more element to dictionary# when we ask value for key which is not in dict then it will print default value
print(res)
print(d1)#setdefault() acts as insert function'''

d3={'a':13, 'b':34}
d3.update(d1)#copies all values of d1 to d3
print(d3)

#to change value for a key
d3['b']=345
d3['p']=2345

#difference between setdefault() and d[index]=value
#both are used to insert value pair to dict
#setdefault() wont change value for the key present in dict
#but d[index]=value will change the value if key is already present
print(d3)

