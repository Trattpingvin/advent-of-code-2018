import string
import pdb

def react(a, b):
	if abs(ord(a)-ord(b)) == 32: #ascii diff between lowercase and uppercase
		return True
	return False

def reduce_polymer(data): #0.42sec
	skipped_indexes = set()
	i = 0
	while i<len(data)-1:
		j = i
		while j in skipped_indexes:
			j -= 1
		current_index = j #first unskipped index backwards from previous
		j = i + 1
		while j in skipped_indexes:
			j += 1
		next_index = j  #first unskipped index forwards from previous+1
		
		if react(data[current_index], data[next_index]):
			skipped_indexes.add(current_index)
			skipped_indexes.add(next_index)
			
		i += 1
	
	ans = ""
	for i, d in enumerate(data): #prettier way to do this? filter maybe?
		if i not in skipped_indexes:
			ans += d
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

