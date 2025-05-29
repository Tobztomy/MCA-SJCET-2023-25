n=int(input("enter the no of numbers"))
a=[]
for i in range(0,n):
    c=int(input(f"enter the number {i+1}: "))
    a.append(c)
print("unsorted list is")
print(a)
for i in range(0, n-1):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            temp = a[j+1]
            a[j+1] = a[j]
            a[j] = temp
print("sorted list is")
print(a)