n=int(input('enter n number'))
n1=2
count=0
while True:
	x=True
	for i in range(2,n1//2+1):
		if n1%i==0:
			x=False
			break
	if x==True:
		print(n1)
		count=count+1 #if given no. is prime no. it will increase count by +1
	if count==n:	  #to check count no. is reached to n number or not
		break
	n1=n1+1