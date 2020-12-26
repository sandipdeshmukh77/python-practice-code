import csv
with open('sandi.csv','r') as f:
    r=csv.reader(f)
    print(r)
    data=list(r)
    print(data)
