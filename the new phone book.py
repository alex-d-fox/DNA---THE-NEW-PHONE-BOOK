import random

class side():
	def __init__(self, top, bottomLeft, bottomRight, center, name):
		self.top = top
		self.bottomLeft = bottomLeft
		self.bottomRight = bottomRight
		self.center = center
		self.name = name
		
class dice():
	def __init__(self, side1,side2,side3,side4):
		self.side1 = side1
		self.side2 = side2
		self.side3 = side3
		self.side4 = side4
		
	def roll(self):
		return random.choice([self.side1,self.side2,self.side3,self.side4]) 
		
g = side(top=1,bottomLeft=2,bottomRight=3,center=4,name="g")
a = side(top=2,bottomLeft=3,bottomRight=4,center=1,name="a")
t = side(top=3,bottomLeft=4,bottomRight=1,center=2,name="t")
c = side(top=4,bottomLeft=1,bottomRight=2,center=3,name="c")		
		
die = dice(g,a,t,c)

for l in range(62460029):
	roll = die.roll()
	z = roll.name
	if z == "g":
		print(z,"a")
	elif z == "a":
		print(z,"g")
	elif z == "t":
		print(z,"c")
	elif z == "c":
		print(z,"t")

