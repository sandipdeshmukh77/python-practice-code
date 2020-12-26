n=int(input('enter the no. of students:'))
d={}
for ch in range(n):
	name=input('eneter student name:')
	marks=int(input('enter students marks:'))
	d[name]=marks
print('student data taken succefully')
print('*'*30)
print('name','\t\t','marks')
print('*'*30)
for k,v in d.items():
	print(k,'\t\t',v)
print('serching operation started....')
while True:
	name=input('enter the student name to find marks')
	marks=d.get(name,-1)
	if marks==-1:
		print('the student not found in the list')
	else:
		print('the mark of',name,'is',marks)
	option=input('do you want to find more students marks(yes/no)')
	if option.lower()=='no':
		break
print("Thank you for using our application")




