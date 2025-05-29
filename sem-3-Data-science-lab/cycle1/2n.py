n = int(input("Enter the number of terms : "))
a = 0;
b = 1;

for i in range(0, n):
    print(a)//0 1 1
    c = a+b//1 2
    a = b//1 1
    b = c//1 2
