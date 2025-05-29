import csv
with open('csv3.csv', newline='') as csvfile:
    d=csv.DictReader(csvfile)
    print("Rollno studentname")
    print("-------------")
    for i in d:
        print(i['Rollno'],i['studentname'])
