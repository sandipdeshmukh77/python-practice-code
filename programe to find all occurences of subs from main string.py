s=input("enter string :-")
subs=input("enter subs to search:-")
i=s.find(subs)
if i==-1:
	print("substring not found")

while i!=-1:
	
	print('{} prensent at index {}'.format(subs,i))
	i=s.find(subs,i+len(subs),len(s))#s.find(subs,begin,end-1)
print("The number of occurance is",s.count(subs))

