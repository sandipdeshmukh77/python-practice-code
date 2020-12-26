fname=input('enter the file name:')
f=open(fname,'w')
while True:
	data=input('enter the data to store in the file:')
	f.write(data+'\n')
	option=input('do you want to store more data [yes/no]')
	if option.lower()=='no':
		break
print('all the data saved to {}.txt successfully')
f.close()

