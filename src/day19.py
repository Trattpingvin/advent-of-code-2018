import pdb

def parse_input(f):
	raw = f.readlines()
	program = []
	ip = int(raw[0][4])
	for i in range(1, len(raw)):
		instruction, a, b, c = raw[i].split()
		program.append((instruction, (int(a), int(b), int(c))))
	return ip, program


class CPU():
	def __init__(self):
		self.state = [0, 0, 0, 0, 0, 0]
		self.ip = 0
		self.program = []
		self.instructions = {"addr" : self.addr, "addi" : self.addi, "mulr" : self.mulr, "muli" : self.muli,
			"banr" : self.banr, "bani" : self.bani, "borr" : self.borr, "bori" : self.bori, "setr" : self.setr, "seti" : self.seti,
			"gtir" : self.gtir, "gtri" : self.gtri, "gtrr" : self.gtrr, "eqir" : self.eqir, "eqri" : self.eqri, "eqrr" : self.eqrr}

	def run(self):
		loops = 0
		
		while True:
			pc = self.state[self.ip]
			if pc<0 or pc>=len(self.program):
				return self.state, loops
			instruction, parameters = self.program[pc]
			self.get_instruction(instruction)(*parameters)
			self.state[self.ip] += 1
			loops += 1
			if loops%1000000==0:
				print loops, self.state

	def get_instruction(self, instruction):
		return self.instructions[instruction]

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


def solvepart1():
	return solvesimplified(950)
	with open('inputs/day19.txt') as f:
		ip, program = parse_input(f)
	cpu = CPU()
	cpu.ip = ip
	cpu.program = program
	return cpu.run()

def solvesimplified(r5):
	#code reduces to problem "sum all divisors of r[5]""

	def divisors(num):
		divisors = []
		smalldiv = 0
		bigdiv = float('inf')
		while smalldiv<bigdiv:
			smalldiv += 1
			if num%smalldiv==0:
				bigdiv = num/smalldiv



				if bigdiv>smalldiv:
					divisors.append(bigdiv)
					divisors.append(smalldiv)
				else:
					if bigdiv==smalldiv:
						divisors.append(smalldiv)
					return divisors

	return sum(divisors(r5))


	

def solvepart2():
	return solvesimplified(10551350)
	with open('inputs/day19.txt') as f:
		ip, program = parse_input(f)
	cpu = CPU()
	cpu.set_state([1, 0, 0, 0 ,0, 0])
	cpu.ip = ip
	cpu.program = program
	return cpu.run()



if __name__=='__main__':
	print solvepart1()
	print solvepart2()

