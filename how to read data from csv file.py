import csv
with open('emp.csv','r') as f:
	r=csv.reader(f)
	l=(list(r))
	for row in l:
		for colum in row:
			print(colum,'\t',end='')
		print()
