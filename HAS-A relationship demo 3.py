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
	def __init__(self,movies,sports,politics):
		self.m=movies
		self.s=sports
		self.p=politics
	def totalnews(self):
		print('the headline are...')
		self.m.moviesinfo()
		self.s.sportsinfo()
		self.p.politicsinfo()
movies=movies()
sports=sports()
politics=politics()
news=news(movies,sports,politics)
news.totalnews()





