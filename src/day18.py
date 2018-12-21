import itertools
import StringIO

def adjacent(coord, areasize):
	x_combo = [-1, 0, 1]
	y_combo = [-1, 0, 1]
	if coord[0]==0: x_combo.remove(-1)
	if coord[1]==0: y_combo.remove(-1)
	if coord[0]==areasize-1: x_combo.remove(1)
	if coord[1]==areasize-1: y_combo.remove(1)

	for p in itertools.product(x_combo, y_combo):
		if p==(0,0): continue
		yield (p[0]+coord[0], p[1]+coord[1])

def readimage(f):
	img = []
	for line in f:
		img.append(line.strip())
	
	return img

def process_rules(acre, startpos, image):
	OPEN = "."
	TREE = "|"
	LUMBERYARD = "#"

	if acre=='.':
		trees = 0
		for x, y in adjacent(startpos, len(image)):
			if image[y][x]==TREE: trees += 1
		if trees>=3:
			return TREE
		return OPEN
	if acre=='|':
		lumberyards = 0
		for x, y in adjacent(startpos, len(image)):
			if image[y][x]==LUMBERYARD: lumberyards += 1
		if lumberyards>=3:
			return LUMBERYARD
		return TREE
	if acre=='#':
		lumberyards = 0
		trees = 0
		for x, y in adjacent(startpos, len(image)):
			if image[y][x]==LUMBERYARD: lumberyards += 1
			elif image[y][x]==TREE: trees += 1
		if lumberyards>=1 and trees>=1:
			return LUMBERYARD
		return OPEN

	print acre
	raise ValueError("bad map")

def tick_minute(image):
	ans = []
	for y, line in enumerate(image):
		next_line = []
		for x, c in enumerate(line):
			next_line.append(process_rules(c, (x, y), image))
		ans.append(next_line)
	return ans

def part1(f):
	img = readimage(f)
	for _ in range(10):
		img = tick_minute(img)

	trees = 0
	lumberyards = 0

	for line in img:
		for c in line:
			if c=="|": trees += 1
			elif c=="#": lumberyards += 1

	return lumberyards*trees

def run_example():
	ex = StringIO.StringIO(""".#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.""")

	return part1(ex)



def solvepart1():
	with open('inputs/day18.txt') as f:
		return part1(f)
		

def solvepart2():
	freq = 0
	seen_freqs = set([freq])
	while True:
		with open('inputs/day1.txt') as f:
			for i in f:
				freq += int(i)
				if freq in seen_freqs:
					return freq
				seen_freqs.add(freq)

	return freq

if __name__=='__main__':
	print run_example()
	print solvepart1()
	print solvepart2()

