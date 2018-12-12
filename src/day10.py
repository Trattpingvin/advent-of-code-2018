import numpy as np

def update_positions(v, steps = 1):
	v[:,0:2] += steps*v[:,2:4]

def solve(vectors):
	"""message should be readable when data is mostly aligned on y-axis. 
	let's find the rate of change of alignment, and print the message when alignment is at its minimum (looks like 8 or 9 from problem description)"""
	v = np.array(vectors)
	stop = 9
	alignment_error1 = max(v[:,1])-min(v[:,1])
	update_positions(v)
	alignment_error2 = max(v[:,1])-min(v[:,1])
	rate_of_change = alignment_error1-alignment_error2

	update_positions(v, (alignment_error2-stop)/rate_of_change)

	msg_start_y = min(v[:,1])
	msg_start_X = min(v[:,0])
	msg_width = max(v[:,0]) - msg_start_X + 1
	msg_height = max(v[:,1]) - msg_start_y + 1 
	
	ans = ""

	grid = np.zeros(shape = (msg_width+1, msg_height+1))
	for vector in v:
		grid[vector[0]-msg_start_X, vector[1]-msg_start_y] = 1


	for y in range(msg_height):
		ans +=''.join("#" if 1==grid[x,y] else "." for x in range(msg_width))
		ans += "\n"

	return ans, (alignment_error1-stop)/rate_of_change

if __name__=='__main__':
	vectors = []
	with open('inputs/day10.txt') as f:
		for line in f:
			
			pos_start = line.find('<')
			pos_end = line.find('>')
			pos = line[pos_start+1:pos_end]
			line = line[pos_end+1:]
			vel_start = line.find('<')
			vel_end = line.find('>')
			vel = line[vel_start+1:vel_end]
			vectors.append([int(i) for i in (pos+","+vel).split(',')])
		
	print solve(vectors)
	
