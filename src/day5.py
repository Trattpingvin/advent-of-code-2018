import string

def react(a, b):
	if abs(ord(a)-ord(b)) == 32: #ascii diff between lowercase and uppercase
		return True
	return False

def reduce_polymer(data):
	
	import pdb

	skipped_index = []
	i = 0
	
	while i<len(data)-1:
		current_index = remaining_index[i]
		next_index = remaining_index[i+1]
		if react(data[current_index], data[next_index]):
			remaining_index.remove(current_index)
			remaining_index.remove(next_index)
			i -=2
			
		i += 1


	ans = ""
	for i in remaining_index:
		ans += data[i]

	return ans, len(ans.strip())

def solvepart1(): #9562, 4934
	with open('inputs/day5.txt') as f:
		data = f.readline()
	
	return reduce_polymer(data)

def solvepart2():
	#pretty slow :/ but no speedup ideas right now


	with open('inputs/day5.txt') as f:
		data = f.readline()

	minpolymerlength = 9999999
	minpolymer = 'none'
	for c in string.ascii_lowercase:
		new_data = data.replace(c, '')
		new_data = new_data.replace(c.upper(), '')
		resdata, resdatalen = reduce_polymer(new_data)
		if resdatalen<minpolymerlength:
			minpolymerlength = resdatalen
			minpolymer = c

	return minpolymer, minpolymerlength

if __name__=='__main__':
	print solvepart1()
	print solvepart2()

