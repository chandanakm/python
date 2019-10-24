lst=[]
n=int(input("enter the number of elements"))
print("enter the elements to sort")
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
print(lst)

for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] > lst[j]:
           lst[i], lst[j] = lst[j], lst[i]
print(lst)
