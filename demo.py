import csv
with open('sandi.csv','w',newline='') as f:
    w=csv.writer(f)
    w.writerow(['ENO','ENAME','ESAL','EADDR'])
    n=int(input('enter number of employee'))
    for i in range(n):
        eno=int(input('enter no'))
        ename=input('enter name')
        esal=float(input('enter salary'))
        eaddr=input('enter address')
        w.writerow([eno,ename,esal,eaddr])
