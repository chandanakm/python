class B:
    address="Bengaluru"
    count=55
    def changeage(self, newage):
        self.empage=newage
    def c1(x,y):
        res=x**y
        return res
    def _B1(p):
        return len(p)
    

class A(B):#inherited all function of B, B is parent class and A is child.
           #multilevel inheritence is possible A(B,C,D)
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

#res=A.B1("ckm")
#print(res)
res1=A.c1(10,3)# c1 is in both class, A will override c1 function.
print(res1)
res2=B.c1(10,3)
print(res2)
res3=B._B1("ckm")
print(res3)
res=obj1.displaysal()
print(res)
