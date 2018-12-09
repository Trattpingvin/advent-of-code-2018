import numpy as np
import pdb
import StringIO
import string

def numberize(c): #make A into 0, B into 1... only owrks on capital letters
	if c in string.ascii_uppercase:
		return ord(c)-65
	raise

def letterize(c): #inverse of numberize
	return chr(c+65)
	
#Step C must be finished before step A can begin.

def read_graph(f):
	seen = set()
	graph = np.zeros((26,26))
	for line in f.readlines():
		i = numberize(line[5])
		j = numberize(line[36])
		seen.add(i)
		seen.add(j)
		graph[i][j] = 1
	graph = graph[0:len(seen),0:len(seen)]
	return graph

def get_open_nodes(graph, indexfilter):
	ans = []
	for i in range(len(graph)):
		if i in indexfilter:
			continue
		if graph[:,i].sum()==0:
			ans.append(i)
	return ans

def mark_completed(graph, i, indexfilter): #release edges going from i since it's completed
	graph[i,:] = 0
	indexfilter.add(i)


def solvepart1():
	example = StringIO.StringIO("""Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.""")

	with open('inputs/day7.txt') as f:
		graph = read_graph(f)
	
	#graph = read_graph(example)
	indexfilter = set()
	ans = ""
	while(len(graph)!=len(indexfilter)):
		node = get_open_nodes(graph, indexfilter)[0]
		mark_completed(graph, node, indexfilter)
		ans += letterize(node)

	return ans

def solvepart2():

	with open('inputs/day7.txt') as f:
		graph = read_graph(f)
	w = 5
	time = 0
	workers = [[-1] for _ in range(w)]
	indexfilter = set()
	workleft = [61+numberize(c) for c in string.ascii_uppercase[:len(graph)]]

	pdb.set_trace()

	while sum(workleft)>0:
		#assign work
		avail = get_open_nodes(graph, indexfilter)
		for work in avail:
			for worker in [w for w in workers if w[0]==-1]:
				worker[0] = work
				indexfilter.add(work)
				break

		#process work
		#find work about to complete
		leastwork = np.inf
		for worker in [w for w in workers if w[0]!=-1]:
			if(workleft[worker[0]])<leastwork:
				leastwork = workleft[worker[0]]
		time += leastwork
		for worker in [w for w in workers if w[0]!=-1]:
			workleft[worker[0]] -= leastwork
			if(workleft[worker[0]]==0):
				mark_completed(graph, worker[0], indexfilter)
				worker[0] = -1

	return time






if __name__=='__main__':
	print solvepart1()
	print solvepart2()

