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

def score(image):
	trees = 0
	lumberyards = 0
	for line in image:
		for c in line:
			if c=="|": trees += 1
			elif c=="#": lumberyards += 1
	return lumberyards*trees


def part1(f):
	img = readimage(f)
	for _ in range(10):
		img = tick_minute(img)

	return score(img)

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

def part2(f):
	img = readimage(f)
	seen_states = [img, score(img)]
	target_gen = 1000000000
	for i in xrange(1, target_gen):
		new_img = tick_minute(img)
		new_score = score(new_img)
		new_state = (new_img, new_score)
		if new_state in seen_states: #cycle found
			cycle_start  = seen_states.index(new_state)
			cycle_length = i - cycle_start +1
			end_cycle_index = (target_gen-cycle_start)%cycle_length
			return seen_states[cycle_start+end_cycle_index+1][1]

		seen_states.append(new_state)
		img = new_img


def solvepart2():
	with open('inputs/day18.txt') as f:
		return part2(f)


if __name__=='__main__':
	print run_example()
	print solvepart1()
	print solvepart2()

