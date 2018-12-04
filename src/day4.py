def solvepart1():
	
	with open('inputs/day4.txt') as f:
		lines = f.readlines()
			
	lines.sort()
	sleeps = {}
	for line in lines:
		splitlines = line.split()
		if "Guard" in line:
			guard_id = splitlines[3]
		else:
			minute = int(splitlines[1][3:5])
			
			if "asleep" in line:
				asleep_time = minute
				
			if "wakes" in line:
				if guard_id not in sleeps:
					sleeps[guard_id] = [0 for _ in range(60)]
				for i in range(minute-asleep_time):
					sleeps[guard_id][asleep_time+i] += 1


	
	maxsleep = 0
	maxguard = ""

	for guard, minutes in sleeps.items():
		
		currentsleep = sum(minutes)
		if currentsleep>maxsleep:
			maxsleep = currentsleep
			maxguard = guard

	return sleeps[maxguard].index(max(sleeps[maxguard])) * int(maxguard[1:])





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

