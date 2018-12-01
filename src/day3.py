def solvepart1():
	freq = 0
	with open('inputs/day1.txt') as f:
		for i in f:
			freq += int(i)
	return freq

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

