n=int(input("enter the limit"))
a=[]
for i in range(0,n):
    c=int(input("enter the number"))
    if c>100:
        a.append("over")
    else:
        a.append(c)
    print(a)