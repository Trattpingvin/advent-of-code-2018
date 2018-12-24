class CPU():
	def __init__(self):
		self.state = [0, 0, 0, 0]
		self.instructions = [self.addr, self.addi, self.mulr, self.muli,
			self.banr, self.bani, self.borr, self.bori, self.setr, self.seti,
			self.gtir, self.gtri, self.gtrr, self.eqir, self.eqri, self.eqrr]

	def get_instruction(self, opcode):
		return self.instructions[opcode]

	def set_state(self, state):
		self.state = state[:]

	def addr(self, a, b, c): 
		self.state[c] = self.state[a] + self.state[b]
		
	def addi(self, a, b, c): 
		self.state[c] = self.state[a] + b
		
	def mulr(self, a, b, c): 
		self.state[c] = self.state[a] * self.state[b]
		
	def muli(self, a, b, c): 
		self.state[c] = self.state[a] * b
		
	def banr(self, a, b, c): 
		self.state[c] = self.state[a] & self.state[b]
		
	def bani(self, a, b, c): 
		self.state[c] = self.state[a] & b
		
	def borr(self, a, b, c): 
		self.state[c] = self.state[a] | self.state[b]
		
	def bori(self, a, b, c): 
		self.state[c] = self.state[a] | b
		
	def setr(self, a, b, c): 
		self.state[c] = self.state[a]
		
	def seti(self, a, b, c): 
		self.state[c] = a
		
	def gtir(self, a, b, c): 
		self.state[c] = 1 if a > self.state[b] else 0
		
	def gtri(self, a, b, c): 
		self.state[c] = 1 if self.state[a] > b else 0
		
	def gtrr(self, a, b, c): 
		self.state[c] = 1 if self.state[a] > self.state[b] else 0
		
	def eqir(self, a, b, c): 
		self.state[c] = 1 if a == self.state[b] else 0
		
	def eqri(self, a, b, c): 
		self.state[c] = 1 if self.state[a] == b else 0
		
	def eqrr(self, a, b, c): 
		self.state[c] = 1 if self.state[a] == self.state[b] else 0
		

def parse_input(f):
	test_cases = []
	while f:
		l1, l2, l3 = f.readline(), f.readline(), f.readline()
		if l1.strip()=="":
			break
		test_case = []
		for line in (l1, l2, l3):
			test_case.append([int(s.strip(",[]")) for s in line.split() if s.strip(",[]").isdigit()])
			
		test_cases.append(test_case)
		f.readline() #trailing empty line
		
	return test_cases

def solvepart1():
	with open('inputs/day16.txt') as f:
		test_cases = parse_input(f)
	cpu = CPU()
	ans = 0

	for test_case in test_cases:
		matches = 0
		for i in range(len(cpu.instructions)):
			cpu.set_state(test_case[0])
			cpu.get_instruction(i)(*test_case[1][1:])
			if cpu.state==test_case[2]:
				matches += 1
				if matches==3:
					ans += 1
					break
	return ans
	

def solvepart2():
	pass

if __name__=='__main__':
	print solvepart1()
	print solvepart2()

