import numpy as np

def getpowerlevel(x, y, serialnumber):
	rack_id = x+ 10
	current = rack_id
	current *= y
	current += serialnumber
	current *= rack_id
	str_current = str(current)
	if len(str_current)<3:
		current = 0
	else:
		current = int(str_current[-3])
	ans = current - 5
	return ans

def solve_naive(serialnumber):
	biggest_sum = 0
	big_x = 0
	big_y = 0
	for x in range(1, 298):
		for y in range(1,298):
			current_sum = sum([getpowerlevel(i+x, j+y, serialnumber) for i in range(3) for j in range(3)])
			if current_sum>biggest_sum:
				biggest_sum = current_sum
				big_x = x
				big_y = y

	return biggest_sum, big_x, big_y


def build_lookup_grid(serialnumber):
	power_grid = np.zeros(shape=(301,301), dtype=np.int)
	for x in range(1,301):
		for y in range(1, 301):
			power_grid[x, y] = getpowerlevel(x, y, serialnumber)

	lookup_grid = np.zeros(shape=(301,301), dtype=np.int)
	for x in range(1,301):
		for y in range(1, 301):
			lookup_grid[x,y] = power_grid[:x,:y].sum()
	return lookup_grid

def lookup_area(grid, x,y,size):#add back the diagonal because it was removed twice by the subtractions
	return grid[x,y]-grid[x-size,y]-grid[x,y-size]+grid[x-size, y-size]

def solve(grid, size):
	biggest_sum = 0
	big_x,big_y = 0, 0
	for x in range(size+1, 300):
		for y in range(size+1, 300):
			current_sum = lookup_area(grid,x,y,size)
			if current_sum>biggest_sum:
				biggest_sum = current_sum
				big_x, big_y = x, y

	return biggest_sum, big_x-size, big_y-size, size

def solvepart1(serialnumber):
	grid = build_lookup_grid(serialnumber)
	return solve(grid, 3)

def solvepart2(serialnumber):
	grid = build_lookup_grid(serialnumber)

	biggest_sum, big_x, big_y, size = 0,0,0,0
	for s in range(1,300):
		cur = solve(grid, s)
		if cur[0]>biggest_sum:
			biggest_sum, big_x, big_y, size = cur
	return biggest_sum, big_x, big_y, size


if __name__=='__main__':

	#print solve_naive(6042)
	#print solvepart1(6042)
	#print solve(6042, 3)
	print solvepart2(6042)

