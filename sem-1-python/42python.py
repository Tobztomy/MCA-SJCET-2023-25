import csv
field_name=['No','company','car model']
car=[{'No':1,'company':'Ferrari','car model':'GH'},
     {'No':2,'company':'BMW','car model':'X5'},
     {'No':3,'company':'Maruti Suzuki','car model':'Swift'},
     {'No':4,'company':'Audi','car model':'RS7'},
     {'No':5,'company':'Toyota','car model':'Fortuner'}]
with open('b.csv','w') as csvfile:
    write=csv.DictWriter(csvfile,fieldnames=field_name)
    write.writeheader()
    write.writerows(car)
with open('b.csv',newline='') as csvfile:
    d=csv.reader(csvfile,delimiter='|')
    for r in d:
        print(','.join(r))