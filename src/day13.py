#41,12 wrong
#41,13 wrong
#147,92 wrong
#147,93 wrong
import operator

def crash(cart, carts):
	crash = 0
	crashed = set()
	for c in carts:
		if cart[0:2] == c[0:2]:
			crashed.add(cart[4])
			crashed.add(c[4])
	if len(crashed)>1:#larger than one because we're also checking against ourselves
		return crashed
	return set() 

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
		carts = [] #cart is tuple: x-coord, y-coord, direction, turning state, id
		i = 0
		for y, line in enumerate(tracks):
			for x, c in enumerate(line):
				if c in dirs:
					carts.append((x, y, dirs.index(c), 0, i))
					i += 1

		loops = 0
		while True:
			carts.sort(key=operator.itemgetter(0))
			carts.sort(key=operator.itemgetter(1))#sort by x first, then y. correct sorting because sort() is stable
			crashed = set()
			for i, cart in enumerate(carts):
				x, y, c, state, cartnum = cart
				if c==0: x += -1
				elif c==1: y += -1
				elif c==2: x += 1
				elif c==3: y += 1

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
					if state==0: c = rot_left(c)
					if state==2: c = rot_right(c)
					state = rot_right(state, 2)

				carts[i] = (x, y, c, state, cartnum)
				crashed = crashed.union(crash(carts[i], carts))
				
				
			for c_i in crashed:
				print str(loops)+": "+str(c)
				for c2 in carts:
					if c2[4]==c_i:
						carts.remove(c2)
						break
			if len(carts)==1:
				return carts

			loops += 1
	except:
		import pdb
		pdb.set_trace()
		raise

if __name__=='__main__':
	with open('inputs/day13.txt') as f:
		print solve(f)
