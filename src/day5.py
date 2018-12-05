import string

def solvepart1():
	def react(a, b):
		if abs(ord(a)-ord(b)) == 32: #ascii diff between lowercase and uppercase
			return True
		return False

	with open('inputs/day5.txt') as f:
		data = f.readline()
	
	i = 0
	import pdb
	while i<len(data)-1:
		if react(data[i], data[i+1]):
			new_data = data[:i]+data[i+2:]
			data = new_data
			i -= 2
		i += 1

	return data, len(data), len(data.strip())

def solvepart2():
	#pretty slow :/ but no speedup ideas right now
	def react(a, b):
		if abs(ord(a)-ord(b)) == 32: #ascii diff between lowercase and uppercase
			return True
		return False

	def reduce_polymer(data):
		i = 0
		while i<len(data)-1:
			if react(data[i], data[i+1]):
				new_data = data[:i]+data[i+2:]
				data = new_data
				i -= 2
			i += 1

		return data, len(data.strip())

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

