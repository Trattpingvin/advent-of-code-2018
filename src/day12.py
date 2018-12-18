from collections import defaultdict
import StringIO
import pdb

def solve(f, generations):
	current_state = f.readline()[15:].strip()
	f.readline() #empty line
	patterns = defaultdict(lambda : ".")#this is used because the example input doesnt include the dots
	for l in f.readlines():
		patterns[l[:5]] = l[9]
	
	zero_index = 0
	next_state = []
	for g in range(generations):
		zero_index += -2
		for i in range(len(current_state)+4):
			found_pattern = ("...."+current_state+"....")[i:i+5]
			assert(len(found_pattern)==5)
			next_state.append(patterns[found_pattern])


		current_state = ''.join(c for c in next_state)
		next_state = []
		#print str(g+1) +": "+ current_state.strip('.')

		
	score = 0
	for i in range(len(current_state)):
		score += zero_index+i if current_state[i]=="#" else 0

	return score



def solvepart1():
	with open('inputs/day12.txt') as f:
		return solve(f, 20)
	return None

def solvepart2():
	scores = []
	
	for i in range(20, 30):
		with open('inputs/day12.txt') as f:
			scores.append(solve(f, i))
		
	for i in range(1, len(scores)):
		print scores[i]
		print scores[i]-scores[i-1]
	with open('inputs/day12.txt') as f:
		last_gen = 45
		return solve(f,last_gen) + 109*(50000000000-last_gen)//2 #manual inspection of output found repetition after generation 28. Score increases by 109 every 2nd generation.

if __name__=='__main__':
	print solvepart1()
	print solvepart2()

