import agents
import random

DEBUG = False

class population :

	def __init__ (self, num, len, binary) :
		self.strings = []
		self.count = num
		self.length = len
		self.binary = binary
		self.total = 0
		self.initialization()
		
	def  initialization (self) :
		for n in range(self.count) :
			string = agents.agent()
			for i in range(self.length) :
				if self.binary :
					string.gene.append(random.randint(0,1))
				else :
					while len(string.gene) < self.length :
						temp = random.randint(1,self.length)
						if string.gene.count(temp) == 0 :
							string.gene.append(temp)
			
			# just for testing (assign random values simulating a run of the game)
			#string.moves = random.randint(4,21)
			#string.result = random.randint(2,4) / 2.0
			
			self.strings.append(string)
			
	def get_pop (self) :
		for i in range(self.count) :
			print "%s distance:%s fitness: %s " % (self.strings[i].gene,self.strings[i].distance,self.strings[i].fitness(10))
			
	
	