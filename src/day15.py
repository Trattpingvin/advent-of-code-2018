import pdb
import StringIO

def alive(it):
	for u in it:
		if u.hp>=0:
			yield u

def adjacent(x, y):
	yield (x, y-1)
	yield (x-1, y)
	yield (x+1, y)
	yield (x, y+1)

class Unit():
	def __init__(self, x, y, type):
		self.x = x
		self.y = y
		self.type = type
		self.hp = 200
		self.ap = 3

	def __repr__(self):
		return "<({}, {}) hp:{}>".format(self.x, self.y, self.hp)

	def take_turn(self, enemies, cave):
		if self.move(enemies, cave): self.attack(enemies, cave)

	def move(self, enemies, cave):
		#move toward nearest enemy. ties resolved in reading order
		#return true is adjacent to enemy

	def attack(self, enemies, cave):

		targets = []
		adj = [adjacent(self.x, self.y)]
		for enemy in alive(enemies):
			if enemy.pos() in adj:
				targets.append(enemy)
		if len(targets==0): raise ValueError("attack called without adjacent targets")
		if len(targets>1):
			targets.sort(key = lambda t : t.x)
			targets.sort(key = lambda t : t.y)
			targets.sort(key = lambda t : t.hp)
		targets[0].hp -= self.ap
		if targets[0].hp <= 0:
			cave[targets[0].y][targets[0].x] = "."
		#attack the target with least HP, ties resolved in reading order
		#check if target died, remove them for cave if so

	def pos(self):
		return (self.x, self.y)

def read_input(f):
	cave = f.readlines()
	elves = []
	goblins = []
	for y, line in enumerate(cave):
		for x, c in enumerate(line):
			if c=='G': goblins.append(Unit(x, y, c))
			elif c=='E': elves.append(Unit(x, y, c))

	return (cave, goblins, elves)



def solvepart1():
	example = StringIO.StringIO("""#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########""")
	cave, goblins, elves = read_input(example)
	units = goblins+elves
	units.sort(key=lambda u: u.x)
	units.sort(key=lambda u: u.y)
	for unit in units:
		unit.take_turn()

def solvepart2():
	pass

if __name__=='__main__':
	print solvepart1()
	print solvepart2()

