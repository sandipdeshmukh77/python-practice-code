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
		self.movies=movies()
		self.sports=sports()
		self.politics=politics()
	def totalnews(self):
		print('the headline are...')
		self.movies.moviesinfo()
		self.sports.sportsinfo()
		self.politics.politicsinfo()
news=news()
news.totalnews()





