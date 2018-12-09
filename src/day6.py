import numpy as np

def find_closest(loc, coords): #-1 for ties
	#make sure they're in the same coordinate system

	closest_dist = np.inf
	closest_pair_index = 0
	hits = 0
	dist = np.abs(loc[:,None] - coords).sum(-1)
#	np.abs(coords-loc)
	import pdb
	pdb.set_trace()
	for i, pair in enumerate(coords):
		x2, y2 = pair[0], pair[1]
		current_dist = abs(x2-x1)+abs(y2-y1)
		if current_dist<closest_dist:
			closest_dist = current_dist
			closest_pair_index = i
			hits = 1
		elif current_dist==closest_dist:
			hits += 1

	if(hits>1): return -1
	return closest_pair_index

def solvepart1():


	coords = np.loadtxt(open('inputs/day6.txt'), delimiter=', ', dtype=np.int)


	xmin, xmax, ymin, ymax = 1000,0,1000,0
	for pair in coords:
		if(pair[0]>xmax): xmax = pair[0]
		if(pair[0]<xmin): xmin = pair[0]
		if(pair[1]>ymax): ymax = pair[1]
		if(pair[1]<ymin): ymin = pair[1]

	shape = (xmax-xmin, ymax-ymin)
	grid = np.zeros(shape, dtype=np.int)

	ans = find_closest(np.where(grid==grid), coords)

	return ans

	for i, _ in np.ndenumerate(grid):
		grid[i] = find_closest(i[0]+xmin,i[1]+ymin,coords)

	bad = reduce(np.union1d,(grid[0], grid[xmax-xmin-1], grid[:,0], grid[:,ymax-ymin-1]))
	
	print bad
	
	valid = False
	ansmax = 0
	for i in range(len(coords)):
		if i in bad:
			continue
		ans = (i==grid).sum()
		if(ans>ansmax):
			ansmax = ans

	return ansmax

def check_friendly_region(x1, y1, coords): 
	
	limit = 10000
	distance_sum = 0
	for pair in coords:
		x2, y2 = pair[0], pair[1]
		current_dist = abs(x2-x1)+abs(y2-y1)
		distance_sum += current_dist
		if distance_sum>=limit:
			return False
	return True

def solvepart2():
	coords = []
	with open('inputs/day6.txt') as f:
		for line in f:
			pair = map(int, line.split(", "))
			coords.append(pair)

	xmin, xmax, ymin, ymax = 1000,0,1000,0
	for pair in coords:
		if(pair[0]>xmax): xmax = pair[0]
		if(pair[0]<xmin): xmin = pair[0]
		if(pair[1]>ymax): ymax = pair[1]
		if(pair[1]<ymin): ymin = pair[1]

	shape = (xmax-xmin, ymax-ymin)
	grid = np.zeros(shape, dtype=np.int)

#	vectorized_f = np.vectorize(find_closest) #TODO RESEARCH
#	vectorized_f(grid)

	for i, _ in np.ndenumerate(grid):
		grid[i] = check_friendly_region(i[0]+xmin,i[1]+ymin,coords)

	return grid.sum()

if __name__=='__main__':
	print solvepart1()
	#print solvepart2()
