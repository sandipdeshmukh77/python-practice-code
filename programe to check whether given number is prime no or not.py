n=int(input("enter number:-"))
if n<=1:
	print('this is not prime number')
else:
	x=True
	for i in range(2,n):
		if n%i==0:
			x=False
			break
	if x==True:
		print("this is prime number")
	else:
		print('this is not prime number')
