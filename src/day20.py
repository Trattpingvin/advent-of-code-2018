import pdb
import StringIO

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


	#find group
	#split members in group
	#call this function on each member

def longest_route(regex):
	if len(regex)<1: return 0
	ans = 0

	#pdb.set_trace()

	stopcount = 0
	startcount = 0
	startindex = 0
	stopindex = 0
	groups = []

	for i, c in enumerate(regex):

		if startcount>0: #we're in matching mode, trying to find the closing parenthesis
			if c=='(':
				startcount += 1
			elif c==')':
				stopcount += 1
				if startcount==stopcount:
					stopindex = i
					ans += longest_route(regex[startindex+1:stopindex])
					startcount, stopcount = 0,0
					groups = []

		else:
			if c=='(': #enter matching mode
				startcount = 1
				startindex = i

				biggest = 0
				groups.append(i)
				for a, b in zip(groups, groups[1:]):
					current = longest_route(regex[stopindex:stopindex+b-a])
					if  current > biggest:
						biggest = current
				ans += biggest
				
			elif c==')':
				raise ValueError("shouldn't happen")

			elif c=='|':
				groups.append(i)

	biggest = 0
	groups.append(i)
	if len(groups)==1: ans += i-stopindex + 1
	else:
		for a, b in zip(groups, groups[1:]):
			current = longest_route(regex[stopindex:stopindex+b-a+1])
			if  current > biggest:
				biggest = current
		ans += biggest

	print "processed regex: "+regex+", decided it's size: "+str(ans)
		

	return ans



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

