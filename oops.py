class A:
    count=0
    def __init__(self, name, age, sal):#__init__ takes input parameters(init is system function)
    #self always stores object name obj1, obj2
        self.empname=name
        self.empage=age
        self.empsal=sal
        print(self.empname, self.empage, self.empsal)
        A.count+=1
    def displaysal(self):#object method
        return self.empsal
    def changename(self, newname):
        self.empname=newname
        return self.empname
    def c1(x,y):#class method
        return x+y
    def c2(x):
        return x.upper()
    def incrementsal(self, newsal):
        self.empsal+=newsal
        return self.empsal
obj1=A('ckm',33,5000)
obj2=A('mkm',32,25000)
obj3=A('snk',33,55000)
print("count:",A.count)


print(obj1.empsal)
print(obj3.empsal)
print(obj1.empage)
res= obj1.displaysal()
print(res)
print(obj1.empname)
res1=obj1.changename('ubr')
print(res1)
res2=A.c1(20,30)
print(res2)
res3=A.c2('ckm')
print(res3)
res4=obj3.incrementsal(55000)
print(res4)
'''normal func'''
