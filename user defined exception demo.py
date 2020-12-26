class ToYoungException(Exception):
	def __init__(self,msg):
		self.msg=msg
class ToOldException(Exception):
	def __init__(self,msg):
		self.msg=msg
age=int(input('enter your age:'))
if age>60:
	raise ToYoungException('wait for some more days you will get best match')
elif age<18:
	raise ToOldException('you are to old to marry, you crossed marrige age')
else:
	print('you will get best match in some days, we will let you know by email')

