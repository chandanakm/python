L1=iter([2,4,6,8,10])
#iterator function is one time usable
#if we use iter() the it will print only once beacause it flushes the value from L1
#this is also called "garbage collector" and also process improvement function.
print(type(L1))#list_iterator
for x in L1:
    print(x)
print("executing second time:")
for y in L1:
    print(y)
