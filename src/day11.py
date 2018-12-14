import numpy as np

def getpowerlevel(x, y, serialnumber):
	#cache doesn't work if power is zero... but no big deal
	global cache
	if cache[x,y]!=0:
		return cache[x,y]
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
	cache[x, y] = ans
	return ans

def solve_naive(serialnumber):
	global cache
	cache = np.zeros(shape=(301, 301))
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



def solve(serialnumber):

	"""pretty aimless idea here... there might be something here - make a grid be sum of something, then an area is a lookup in the grid minus another looksup. sum of what though?"""
	power_sums_x = np.zeros(shape=(301, 301))
	for x in range(1,301):
		for y in range(1, 301):
			power_sums_x[x, y] = getpowerlevel(x, y, serialnumber) + power_sums_x[x-1,y]


	biggest_sum = 0
	big_x, big_y = 0, 0
	power_sums_y = np.zeros(301)
	for x in range(4,301):
		for y in range(4, 301):
			current_sum = power_sums[x,y]-power_sums[x-3, y]
			power_sums_y[x] = current_sum



	return biggest_sum, big_x, big_y


if __name__=='__main__':
	print solve_naive(6042)

