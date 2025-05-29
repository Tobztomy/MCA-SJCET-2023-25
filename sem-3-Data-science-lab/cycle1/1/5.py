print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
for num in range(1, 1000 + 1):
    order = len(str(num))
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10

    if num == sum:
        print(num)
