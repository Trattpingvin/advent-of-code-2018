class Node():
	def __init__(self, val, prevNode=None, nextNode=None):
		self.prevNode = prevNode
		self.nextNode = nextNode
		self.val = val

	def delete(self):
		self.prevNode.nextNode = self.nextNode
		self.nextNode.prevNode = self.prevNode

def marblegame(players, marbles): # 0 1 None
	
	root = Node(0)
	root.prevNode = root
	root.nextNode = root
	current = root

	scoreboard = [0]*players

	for i in range(1, marbles+1):

		if i%23==0:
			#backwards seven times
			for _ in range(7):
				current = current.prevNode
			toDelete = current
			current = current.nextNode
			scoreboard[i%players] += i + toDelete.val
			toDelete.delete()


		else:
			#forward twice   0 8 4 2 5 1 6 3 7
			for _ in range(1): 
				current = current.nextNode
			prev_nextNode = current.nextNode
			new = Node(i, current, prev_nextNode)
			prev_nextNode.prevNode = new
			current.nextNode = new
			current = new


		if i%100000==0:
			print i
		
	#ll = root
	#for i in range(marbles):
		#print ll.val
		#ll = ll.nextNode
	print "\n\n"
	return max(scoreboard)



def solvepart1():
	#return marblegame(493,71863)
	return marblegame(431,70950*100)

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
	#print solvepart2()

