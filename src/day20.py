def parse_branches(regex):
	
	ans = []
	stopcount = 0
	startcount = 0
	startindex = 0
	for i, c in enumerate(regex):
		if c=='(':
			if startcount==0:
				startindex = i
				startcount += 1
		elif c==')':
			stopcount += 1
			if startcount==stopcount:
				stopindex = i
#				ans.append(regex[:startindex]parse_branches(regex[startindex:stopindex]))



def longest_route(regex):

	startcount = 0
	startindex = 0
	stopcount = 0
	backtrack = False

	groups = []
	current = 0

	for i, c in enumerate(regex):
		if startcount>0: #trying to match a parenthesis
			if c=='(':
				startcount += 1
			elif c==')':
				stopcount += 1
				if stopcount == startcount:

					groupsize, bt = longest_route(regex[startindex+1:i]) #if this route contains empty |, we want the max of this and the rest of our length
					if bt:
						groups.append(current)
						ans = max(groups)
						
						if 0 in groups:
							backtrack = True
						

						ans = max(groups) + max(groupsize/2, longest_route(regex[i+1:])[0]), backtrack
						print "processed regex: "+regex+", decided it's: "+str(ans)
						print groups
						return ans
					else:
						current += groupsize
					startcount = 0
					startindex = 0
					stopcount = 0

		else:
			if c=='(':
				startcount = 1
				startindex = i

			elif c=='|':
				groups.append(current)
				current = 0
			else:
				current += 1

	groups.append(current)
	ans = max(groups)

	if 0 in groups:
		backtrack = True
	print "processed regex: "+regex+", decided it's: "+str((ans, backtrack))
	print groups
	return ans, backtrack



def parse_data(f):
	data = f.readline()
	return data.strip("^$\n")

def run_examples():
	examples = []
	examples.append((StringIO.StringIO("""^ENWWW(NEEE|SSE(EE|N))$"""), 10))
	examples.append((StringIO.StringIO("""^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"""), 18))
	examples.append((StringIO.StringIO("""^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"""), 23))
	
	for example, expected_ans in examples:
		data = parse_data(example)
		ans = longest_route(data)

		print "Example ran. Expected: "+str(expected_ans)+", got: "+str(ans)

	


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
	run_examples()
	#print solvepart1()
	#print solvepart2()

