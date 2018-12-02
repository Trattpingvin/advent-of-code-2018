import string

def solvepart1():
	counts = [0, 0]
	with open('inputs/day2.txt') as f:
		for line in f:
			for i in [2,3]:
				for c in string.ascii_lowercase:
					if(string.count(line, c)==i):
						counts[2-i] += 1
						break

	return counts[0]*counts[1]

def solvepart2():
	with open('inputs/day2.txt') as f:
		inputs = f.readlines()
		
	for line1_index in range(len(inputs)):
		distance = [0 for _ in range(len(inputs))]
		l1 = inputs[line1_index]
		for line2_index in range(len(inputs)):
			l2 = inputs[line2_index]
			for i in range(len(inputs[0])): #every input has the same length
				if l1==l2:
					distance[line2_index] = 20 #dummy value to enable use of min
					break
				if(l1[i]!=l2[i]):
					distance[line2_index] += 1
				if distance[line2_index]>1:
					break
		if (min(distance)==1):
			differing_index = distance.index(1)
			word1 = l1
			word2 = inputs[distance.index(1)]
			ans = ""
			for i in range(len(word1)):
				if word1[i]==word2[i]:
					ans += word1[i]
			return ans

if __name__=='__main__':
	print solvepart1()
	print solvepart2()

