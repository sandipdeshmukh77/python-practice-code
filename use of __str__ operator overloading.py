class book:
	def __init__(self,pages):
		self.pages=pages
	def __add__(self,other):
		return book(self.pages+other.pages)
	def __str__(self):
		return 'the number of pages are:{}'.format(self.pages)
b1=book(100)
b2=book(200)
b3=book(300)
print(b1+b2)
print(b1+b2+b3)