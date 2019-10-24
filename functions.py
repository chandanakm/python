'''print("user defined functions")
name="ckm"
def test(x,y,z):#required and positional arguments
    res=x+y+z
    global age
    age=40 #making age as global
    print("name is:",name)
    return res

op=test(20,10,5)
print(op)
print(age)
------------------------------------------------------------------------
print("user defined functions")
name="ckm"
def test(x,y,z):#required and non-positional keyword arguments
    res=x+y+z
    global age
    age=40 #making age as global
    print("name is:",name)
    return res

op=test(z=20,x=10,y=5)
print(op)
print(age)
------------------------------------------------------------------------

print("user defined functions")
name="ckm"
def test(x,y,z=500):#default argument function, here sending z values as 500 by default, it takes default value only when there is no value given.
    res=x+y+z
    global age
    age=40 #making age as global
    print("name is:",name)
    return res

op=test(y=20,z=10,x=5)#if we pass value for z here also, it wont take default value
print(op)
print(age)

#def test(x,y=200,z): we cannot pass a default argument before non-default value
--------------------------------------------------------------------------------------
print("user defined functions")
name="ckm"
def test(x,y,z):#having multiple return statement
    res=x+y+z
    global age
    age=40 #making age as global
    print("name is:",name)
    return res,"ckm"#function can have only one return statement and we can pass multiple values.
    return "ckm"#not valid

op=test(z=20,x=10,y=5)
print(op)
print(age)
----------------------------------------------------------------------------------------------
print("user defined functions")
name="ckm"
def test(x,y,*z,a=100):#'*'is used to assign all remaining values to z as tuple.
   print(x)
   print(y)
   print(z)
   print(a)

test(1,2,3,4,5)
------------------------------------#variable length arguments 1. *args and 2. **args(kwargs)
print("user defined functions")
name="ckm"
def test(x,y,**z):#'**'is used when there is a key-value pair like a=1, b=2
   print(x)
   print(y)
   print(z)
   

test(x=1,y=2,z=3,a=4,b=5)# max() function uses variable length function because it takes any number of input
