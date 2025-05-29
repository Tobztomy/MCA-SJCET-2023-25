print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
n = int(input("Enter the number of terms : "))
a = 0;
b = 1;
for i in range(0, n):
    print(a)
    c = a+b
    a = b
    b = c
