class book:
	def __init__(self,pages):
		self.pages=pages
	def __add__(self,other):
		total_pages=self.pages+other.pages
		return total_pages
b1=book(100)
b2=book(200)
print(b1+b2)