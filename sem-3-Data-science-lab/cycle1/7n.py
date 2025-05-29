num = input("Enter a mobile number : ")
absent = sorted(set('0123456789') - set(num))
print(absent)


