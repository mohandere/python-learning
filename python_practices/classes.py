class Dog:


	def __init__(self, name):
		self.name = name
		self.tricks = []


	def add_trick(self, trick):
		self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Tommy')

print d.name
print e.name

print "------------"

d.add_trick('My')
e.add_trick('Love')


print d.tricks
print e.tricks


