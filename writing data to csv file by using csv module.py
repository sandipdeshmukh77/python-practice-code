import csv
with open('emp.csv','w',newline='') as f:
	w=csv.writer(f)
	w.writerow(['ENO','ENAME','ESAL','EADDR'])
	while True:
		eno=int(input('enter employee number:-'))
		ename=input('enter employee name:-')
		esal=float(input('enter empolyee salary:-'))
		eaddr=input('enter employee address:-')
		w.writerow([eno,ename,esal,eaddr])
		option=input('do you want to add more employee data[yes/no]:-')
		if option.lower()=='no':
			break
print('the employee data saved successfully')


