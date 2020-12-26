x=int(input('enter the number of students:-'))
d={}
for i in range(x):
	name=input("enter the stundent name:-")
	marks=int(input('enter the marks of student:-'))
	d[name]=marks
print('*'*30)
print('name','\t\t','marks')
print('*'*30)
for z in d:
	print(z,'\t\t',d[z])

