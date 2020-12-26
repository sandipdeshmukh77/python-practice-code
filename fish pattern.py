print('\n\n\n\n')
print('\t\t\t\t\t')
for r in range(0,10):
	for c in range(0,12):
		if ((r==0 or r==9) and c==5) or ((r==1 or r==8) and (c==4 or c==5))\
		   or ((r==2 or r==7) and c in(2,3,4,5,6,7,11))\
		   or ((r==3 or r==6) and c in(1,2,8,10,11))\
		   or ((r==4 or r==5) and c in(0,3,9,11)):
			   print('*',end='')
		else:
			print(end=' ')
	print()
