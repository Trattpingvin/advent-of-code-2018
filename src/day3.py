import re

def solvepart1():
	shape = 1100 #from visual inpsection of input
	occupied = [[0 for i in range(shape)] for j in range(shape)]
	with open('inputs/day3.txt') as f:
		for line in f:
			splitlines = line.split()
			x, y = splitlines[2].split(',')
			w, h = splitlines[3].split('x')
			y = y[:-1] # remove the colon

			x,y,w,h = map(int, (x, y, w, h))
			
			for i in range(w):
				for j in range(h):
					occupied[x+i][y+j] += 1


	ans = 0
	for i in range(shape):
		for j in range(shape):
			if occupied[i][j]>1:
				ans += 1

	return ans
			
			
			
		

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

