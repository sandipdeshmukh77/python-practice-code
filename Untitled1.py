n=int(input('enter a number between 0-99:'))
list1= ['', 'one','two', 'three','four','five','six','seven','eight','nine','ten','eleven',
'twevel','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','ninteen']
list2= ['','','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
if n==0:
	output='zero'
elif n<=19:
	output=list1[n]
elif n<=99:
	output=list2[n//10]+' '+ list1[n%10]
print(output)