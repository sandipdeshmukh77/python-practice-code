years=int(input('enter no. of years:'))
amount=float(input('enter amount:'))
output=amount
for i in range(3,years,3):
	output=output*2
print('the total return you will get is',output)