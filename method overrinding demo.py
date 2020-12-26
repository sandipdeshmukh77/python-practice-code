class parents:
	def property(self):
		print("gold+money+cash")
	def marry(self):
		print('karina')
class child(parents):
	def marry(self):
		super().marry()
		print('katrina')
c=child()
c.property()
c.marry()