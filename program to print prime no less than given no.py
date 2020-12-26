n=int(input('enter any number'))
n1=2
while n1<=n:#this will print number 2,3,4.....10 to check whether it is prime or not
	x=True
	for i in range(2,n1//2+1):
		if n1%i==0:
			x=False
			break
	if x==True:
		print(n1)
	n1=n1+1