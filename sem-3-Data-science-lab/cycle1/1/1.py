print("SJC23MCA-2059 : TOBIN K TOMY")
print("Batch : MCA 2023-25")
lower_value = int(input("Please, Enter the Lowest Range Value: "))
upper_value = int(input("Please, Enter the Upper Range Value: "))

print("The Non-Prime Numbers in the range are:")

for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(number)
                break
