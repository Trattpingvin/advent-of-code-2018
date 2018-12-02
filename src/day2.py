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

