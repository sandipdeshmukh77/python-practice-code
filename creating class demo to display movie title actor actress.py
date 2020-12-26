class movie:
	def __init__(self,title,actor,actress):
		self.title=title
		self.actor=actor
		self.actress=actress

	def info(self):
		print('the movie name is',self.title)
		print('the actor in movie is',self.actor)
		print('the actress in movie is',self.actress)

list_of_movies=[]
while True:

	title=input('enter movie name:')
	actor=input('enter the name of actor:')
	actress=input('enter the name of actress:')
	m=movie(title,actor,actress)
	list_of_movies.append(m)
	print('movie added succesfully')
	option=input('do you want to add more movie[yes/no]:')
	if option.lower() =='no':
		break
for m in list_of_movies:
	m.info()
	print()





