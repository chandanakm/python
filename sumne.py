'''print("user defined functions")
name="ckm"
def test(x,y,**z):#'**'is used when there is a key-value pair like a=1, b=2
   print(x)
   print(y)
   print(z)
   

test(x=1,y=2,z=3,a=4,b=5)# max() function uses variable length function because it takes any number of input

print("user defined functions")
name="ckm"
def test(x,y,*z,a=100):#'*'is used to assign all remaining values to z as tuple.
   print(x)
   print(y)
   print(z)
   print(a)

test(1,2,3,4,5)
'''
