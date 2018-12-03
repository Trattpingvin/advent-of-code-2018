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

	def verify_overlap(x, y, w, h):
		for i in range(w):
			for j in range(h):
				if(occupied[x+i][y+j]!=1):
					return False
		return True
		
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

	with open('inputs/day3.txt') as f:
		for line in f:
			splitlines = line.split()
			x, y = splitlines[2].split(',')
			w, h = splitlines[3].split('x')
			y = y[:-1] # remove the colon
			claim = splitlines[0]

			x,y,w,h = map(int, (x, y, w, h))
			if(verify_overlap(x,y,w,h)):
				return claim
			

	
	

if __name__=='__main__':
	print solvepart1()
	print solvepart2()

