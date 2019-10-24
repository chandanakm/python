def gen(f,x,y,p):
    fvar=open(f,'r')
    data=fvar.read()
    fvar.close()
    res='success' in data
    if(res== True):
        yield "success"
    else:
        yield "error"

    res2=x+y
    yield res2

    res3=p.upper()
    yield res3
    yield "complete"

op=gen(r'D:\Desktop\ret.txt',20,60,'sandy')
op1=next(op)
if(op1=="success"):
    print("file is success file, calling return")
    op2=next(op)
    if(op2>50):
        print("calling third return")
        op3=next(op)
        if(op3.isupper()== True):
            print("calling fiurth return")
            op4=next(op)
            print(op4)
        else:
            print("stopped at third return")
    else:
        print("stopped at second return")
else:
    print("file is error file")

