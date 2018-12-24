import pdb

class CPU():
	def __init__(self):
		self.state = [0, 0, 0, 0]
		self.instructions = [self.addr, self.addi, self.mulr, self.muli,
			self.banr, self.bani, self.borr, self.bori, self.setr, self.seti,
			self.gtir, self.gtri, self.gtrr, self.eqir, self.eqri, self.eqrr]
		self.assignment = None

	def get_instruction(self, opcode):
		if self.assignment: 
			return self.instructions[self.assignment[opcode]]
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
	program = []
	while f:
		l1 = f.readline()
		if l1.strip()=="":
			break
		test_case = []
		for line in (l1, f.readline(), f.readline()):
			test_case.append([int(s.strip(",[]")) for s in line.split() if s.strip(",[]").isdigit()])
			
		test_cases.append(test_case)
		f.readline() #trailing empty line

	f.readline()

	program = f.readlines()	

	return test_cases, program

def solvepart1():
	with open('inputs/day16.txt') as f:
		test_cases, _ = parse_input(f)
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
	with open('inputs/day16.txt') as f:
		test_cases, program = parse_input(f)
	
	cpu = CPU()
	valid = [(1<<16)-1 for _ in range(len(cpu.instructions))]


	for test_case in test_cases:
		before, command, after = test_case
		current_opcode = command[0]
		for i in range(len(cpu.instructions)):
			if valid[i]&1<<current_opcode == 0: continue
			cpu.set_state(before)
			cpu.get_instruction(i)(*command[1:])
			if cpu.state!=after:
				valid[i] -= 1<<current_opcode

	assigned = [i for i in range(16)]
	unassigned = [i for i in range(16)]

	while len(unassigned)>0:
		for i, valids in enumerate(valid):
			if i not in unassigned: continue
			if bin(valids).count("1") == 1:
				opcode = 0
				while valids>1:
					valids = valids>>1
					opcode += 1
				assigned[opcode] = i
				unassigned.remove(i)
				#pdb.set_trace()
				for j in range(16):
					if valid[j]&1<<opcode != 0:
						valid[j] -= 1<<opcode
				break

	cpu.assignment = assigned
	cpu.set_state([0, 0, 0 ,0])
	for line in program:
		line = line.strip()
		opcode, a, b, c = map(int, line.split())
		cpu.get_instruction(opcode)(*(a, b, c))

	return cpu.state[0]

		

if __name__=='__main__':
	print solvepart1()
	print solvepart2()

