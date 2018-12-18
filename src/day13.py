def crash(cart, carts):
	crash = 0
	for c in carts:
		if cart[0:2] == c[0:2]:
			crash += 1
	return crash>1 #larger than one because we're also checking against ourselves

def rot_right(index, wrap = 3):
	if index==wrap:
		return 0
	return index+1

def rot_left(index):
	if index==0:
		return 3
	return index-1


def solve(f):
	try:
		tracks = f.readlines()
		dirs = "<^>v"
		carts = [] #cart is tuple: x-coord, y-coord, direction, turning state
		for y, line in enumerate(tracks):
			for x, c in enumerate(line):
				if c in dirs:
					carts.append((x, y, dirs.index(c), 0))

		loops = 0
		while True:
			for i, cart in enumerate(carts): #we have t o do this in order. probably sort it first?
				x, y, c, state = cart
				if c==0: x += -1
				if c==1: y += -1
				if c==2: x += 1
				if c==3: y += 1

				if tracks[y][x] == '/':
					if c==0: c = rot_left(c)
					elif c==1: c = rot_right(c)
					elif c==2: c = rot_left(c)
					elif c==3: c = rot_right(c)

				if tracks[y][x] == '\\':
					if c==0: c = rot_right(c)
					elif c==1: c = rot_left(c)
					elif c==2: c = rot_right(c)
					elif c==3: c = rot_left(c)
					
				if tracks[y][x] == '+':
					if state==0:
						c = rot_left(c)
					if state==2:
						c = rot_right(c)
					state += 1
					if state==3:
						state = 0

				carts[i] = (x, y, c, state)
				if crash(carts[i], carts):
					return (x,y)

			loops += 1
	except:
		import pdb
		pdb.set_trace()


def solvepart1():
	with open('inputs/day13.txt') as f:
		return solve(f)
	

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
	print solvepart1()
	print solvepart2()

