class  movies:
	def moviesinfo(self):
		print('the movie news')
		print('the movie news')
		print('the movie news')
class sports:
	def sportsinfo(self):
		print('sport news')
		print('sport news')
		print('sport news')
class politics:
	def politicsinfo(self):
		print('politics news')
		print('politics news')
		print('politics news')
class news:
	def __init__(self):
		self.m=movies()
		self.s=sports()
		self.p=politics()
	def totalnews(self):
		print('the headline are...')
		self.m.moviesinfo()
		self.s.sportsinfo()
		self.p.politicsinfo()
news=news()
news.totalnews()





