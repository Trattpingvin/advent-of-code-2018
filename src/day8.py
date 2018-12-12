import numpy as np
import pdb
import StringIO
import string



def solve(f): 
	def rec(data):  #return index of where headers data ends, and sum of metadata
		if len(data)<2:
			return 0,0
		num_children = data[0] 
		num_metadata = data[1] 
		total_sum = 0
		index = 2
		for c in range(num_children):
			new_index, new_sum = rec(data[index:])
			index += new_index
			total_sum += new_sum
		for m in range(num_metadata):
			total_sum += data[index]
			index += 1
		return index, total_sum
	data = np.loadtxt(f, delimiter=' ', dtype=np.int)

	return rec(data)[1]


def solvepart1():
	
	example = StringIO.StringIO("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")

	with open('inputs/day8.txt') as f:
		return solve(f)

	return solve(example)

def solvepart2():

	def rec(data):  #return index of where headers data ends, and sum of metadata
		if len(data)<2:
			return 0,0
		num_children = data[0] 
		num_metadata = data[1] 
		value = 0
		index = 2
		children = []

		for c in range(num_children):
			child = rec(data[index:])
			children.append(child)
			index += child[0]
			
		for _ in range(num_metadata):
			metadata = data[index]
			if num_children==0:
				value += metadata
			else:
				if metadata>0 and metadata<=len(children):
					value += children[metadata-1][1]
			index += 1
		return index, value



	f = StringIO.StringIO("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2")

	with open('inputs/day8.txt') as f:
		data = np.loadtxt(f, delimiter=' ', dtype=np.int)
	
	return rec(data)[1]

if __name__=='__main__':
	print solvepart1()
	print solvepart2()


