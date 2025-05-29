num=int(input("enter the number"))
list=[i for i in range(1,num+1) if num % i==0]
print("factors of number=",list)