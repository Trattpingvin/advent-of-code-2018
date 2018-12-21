import pdb
import StringIO
import collections

#204960 too low
#207120 too low

def alive(it):
	for u in it:
		if u.hp>0:
			yield u

def adjacent(x, y):
	yield (x, y-1)
	yield (x-1, y)
	yield (x+1, y)
	yield (x, y+1)

def shortest_path(cave, startx, starty, target):
	#returns step necessary to reach closest enemy, tupled with distance to that enemy
	try:
		i = 0
		current = [(coord, coord) for coord in adjacent(startx, starty)] #list of tuples indicating where we should look, and which step we took to get there
		already_queued = set(adjacent(startx, starty))
		already_queued.add((startx, starty))
		while(len(current)>0):
			current.sort(key = lambda coord : coord[0][0])
			current.sort(key = lambda coord : coord[0][1])
			found = list()
			while(len(current)>0):
				cur, first_step = current.pop(0)
				x, y = cur
				if cave[y][x] == target:
					return (first_step[0]-startx, first_step[1]-starty), i
				elif cave[y][x] == ".":
					new_tiles = [(adj, first_step) for adj in adjacent(x,y) if adj not in already_queued]
					for t in new_tiles:
						found.append(t)	
						already_queued.add(t[0])

			current = [c for c in found]
			i += 1
	except:
		pdb.set_trace()
		raise

	return (0,0), float('inf')






class Unit():
	def __init__(self, x, y, type, ap = 3):
		self.x = x
		self.y = y
		self.type = type
		self.hp = 200
		self.ap = ap

	def __repr__(self):
		return "<{}({}, {}) hp:{}>".format(self.type, self.x, self.y, self.hp)

	def take_turn(self, enemies, cave):
		if self.hp<=0: return
		if self.move(enemies, cave): self.attack(enemies, cave)

	def move(self, enemies, cave):
		assert(cave[self.y][self.x]==self.type)
		if len(list(alive(enemies)))==0:
			return False
		adj = list(adjacent(self.x, self.y))
		for enemy in alive(enemies):
			if enemy.pos() in adj:
				return True #don't move if we are already in attack range
		#move toward nearest enemy. ties resolved in reading order
		#return true is adjacent to enemy
		direction, length = shortest_path(cave, self.x, self.y, "E" if self.type=="G" else "G")
		cave[self.y][self.x] = "."
		self.x += direction[0]
		self.y += direction[1]
		cave[self.y][self.x] = self.type
		if length==1:
			return True
		return False


	def attack(self, enemies, cave):

		targets = []
		adj = list(adjacent(self.x, self.y))
		for enemy in alive(enemies):
			if enemy.pos() in adj:
				targets.append(enemy)
		if len(targets)==0: raise ValueError("attack called without adjacent targets")
		if len(targets)>1:
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

def read_input(f, elf_attackpower = 3):
	cave = []
	for line in f.readlines():
		cave.append(list(line))
	elves = []
	goblins = []
	for y, line in enumerate(cave):
		for x, c in enumerate(line):
			if c=='G': goblins.append(Unit(x, y, c))
			elif c=='E': elves.append(Unit(x, y, c, elf_attackpower))

	return (cave, goblins, elves)


def test_examples():

	examples = []
	examples.append((StringIO.StringIO("""#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######
"""), 36334))

	examples.append((StringIO.StringIO("""#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""), 27730))

	examples.append((StringIO.StringIO("""#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######
"""), 39514))

	examples.append((StringIO.StringIO("""#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######
"""), 27755))

	examples.append((StringIO.StringIO("""#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""), 28944))

	examples.append((StringIO.StringIO("""#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.#
#########"""), 18740))

	for i, pair in enumerate(examples):
		example, expected = pair
		ans = run_simulation(example)[0]
		print "Example {} {}".format(i+1, "passed" if ans==expected else "expected "+str(expected)+" but got "+str(ans))


def run_simulation(f, elf_attackpower = 3):
	cave, goblins, elves = read_input(f, elf_attackpower)
	loops = 0
	try:
		while(len(goblins)>0 and len(elves)>0):
			units = goblins+elves
			units.sort(key=lambda u: u.x)
			units.sort(key=lambda u: u.y)
			
			for unit in units:
				unit.take_turn(goblins if unit.type=="E" else elves, cave)
			to_delete = []
			for g in goblins:
				if g.hp<=0:
					to_delete.append(g)
			for g in to_delete:
				goblins.remove(g)
			to_delete = []
			for e in elves:
				if e.hp<=0:
					to_delete.append(e)
			for e in to_delete:
				elves.remove(e)


			loops += 1
	except:
		pdb.set_trace()
		raise
	#pdb.set_trace()
	return (loops-1)*sum([u.hp for u in goblins+elves]), len(elves)


def solvepart1():
	with open("inputs/day15.txt") as f:
		return run_simulation(f)
		
def solvepart2():
	num_starting_elves = 0
	with open("inputs/day15.txt") as f:
		for line in f:
			for c in line:
				if c=="E": num_starting_elves += 1

	elf_attackpower = 3
	while True:
		print "running simulation with attackpower "+str(elf_attackpower)
		elf_attackpower += 1
		with open("inputs/day15.txt") as f:
			ans = run_simulation(f, elf_attackpower)
		if ans[1] == num_starting_elves:
			return ans[0]

	

if __name__=='__main__':
	test_examples();
	print solvepart1()
	print solvepart2()

