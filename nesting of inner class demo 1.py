class human:
	def __init__(self,name):
		print('execution of human class')
		self.name=name
		self.head=self.head() #this will call "human.head()"
	def info(self):
		print('hello myself',self.name)
		print('i am sofware engineer')
		self.head.talk()
		self.head.brain.think()
	class head:
		def __init__(self):
			print('execution of head class')
			self.brain=self.brain() #this will call "head.brain()"
		def talk(self):
			print('talking')
		class brain:
			def __init__(self):
				print('execution of brain class')
			def think(self):
				print("thinking")
h=human('san')
h.info()

