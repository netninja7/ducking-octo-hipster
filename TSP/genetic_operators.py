import random
import agents

DEBUG = False

class gen_op :

	def __init__ (self, pop, Pc, Pm) :
		self.pop 		= pop
		self.total 		= 0
		self.CDF		= []
		self.intgen 	= []
		self.newpop 	= []
		self.Pc			= Pc
		self.Pm			= Pm
		
	def run_gen (self) :	
		self.pop_sum()
		self.calc_proportion_val()
		self.calc_CDF()
		self.intermediate_gen()
		self.select_maters()
		
	def next_gen(self) :
		self.single_point_cross()
		self.mutation_mix()
		self.swap_new()
		self.clear()
	
	def clear(self) :
		self.total 		= 0
		self.CDF		= []
		self.intgen 	= []
		self.newpop 	= []
	
	def pop_sum (self) :
		for agent in self.pop.strings :
			self.total += agent.fitness(self.pop.length)
		
	# TODO : Combine following functions into one loop to save processing time
	def calc_proportion_val (self) :
		for i in range(self.pop.count) :
			self.pop.strings[i].value = (self.pop.strings[i].result / self.total)
		
	def calc_CDF (self) :
		tmp_total = 0
		for i in range(self.pop.count) :
			self.CDF.append(self.pop.strings[i].value + tmp_total)
			tmp_total += self.pop.strings[i].value
		if DEBUG :
			print self.CDF
		
	def intermediate_gen (self) :
		for n in range(self.pop.count) :
			num = random.random()
			for i in range(self.pop.count) :
				if num <= self.CDF[i] :
					keep = i
					break
			tmp_agent = agents.agent()
			tmp_agent.load_gene(self.pop.strings[keep].gene[:])
			self.intgen.append(tmp_agent)
			
	def select_maters (self) :
		maters = self.pop.count
		for i in range(self.pop.count) :
			num = random.random()
			if num <= self.Pc :
				self.intgen[i].replicate = True
				maters -= 1
		if DEBUG :
			print "Non maters: %s" % (maters)
	
	
	
	def single_point_cross (self) :
		while len(self.intgen) != 0 :
			# ident parents
			male 	= None
			female 	= None 
			for i in self.intgen :
				if i.replicate :
					if len(self.intgen) == 1 : #places the odd numbered mater into the next generation
						i.replicate = False
						self.newpop.append(self.intgen.pop(self.intgen.index(i)))
					elif male == None :
						male 	= i
					elif female == None  and female != i :
						female 	= i
						break
				else :
					self.newpop.append(self.intgen.pop(self.intgen.index(i)))

			# Mate strings
			if male != None and female != None :
				self.intgen.remove(male)
				self.intgen.remove(female)
				tmp_male = []
				tmp_female = []
				crossover = random.randint(0,self.pop.length-1)
				# crossover = 9 # Define a crossover point
				# print crossover
				if self.pop.binary: # Binary single point crossover
					for i in range(1,crossover) :
						tmp_female.append(female.gene.pop())
						tmp_male.append(male.gene.pop())
					for m in range(1,crossover) :
						male.gene.append(tmp_female.pop())
						female.gene.append(tmp_male.pop())
				else: 	# Single point "order crossover"
					for i in male.gene[crossover:] :
						tmp_male.append(i)
					for i in male.gene[:crossover] :
						tmp_male.append(i)
					for i in female.gene[crossover:] :
						tmp_female.append(i)
					for i in female.gene[:crossover] :
						tmp_female.append(i)
					for i in male.gene[crossover:] :
						male.gene.pop()
						female.gene.pop()
					for i in tmp_female :
						if female.gene.count(i) == 0 :
							female.gene.append(i)
					for i in tmp_male :
						if male.gene.count(i) == 0 :
							male.gene.append(i)

				male.replicate = False
				female.replicate = False
				self.newpop.append(male)
				self.newpop.append(female)

	def mutation_random (self) :  #randomly mutates swapping two locations
		for i in range(self.pop.count) :
			temp = agents.agent()
			s = 0
			num = random.random()
			if num <= self.Pm :
				first = random.randint(0,self.pop.length-1)
				second = random.randint(0,self.pop.length-1)
				temp.gene[:] = self.newpop[i].gene[:]
				s = temp.gene[first]
				temp.gene[first] = temp.gene[second]
				temp.gene[second] = s
				self.newpop[i].gene[:] = temp.gene[:]
					
	def mutation_improve (self) : #only mutates if the swapping will produce a better fitness
		for i in range(self.pop.count) :
			changed = False
			count = 0
			highest = 0
			temp = agents.agent()
			s = 0
			num = random.random()
			if num <= self.Pm :
				while count < 10 and not changed:
					first = random.randint(0,self.pop.length-1)
					second = random.randint(0,self.pop.length-1)
					temp.gene[:] = self.newpop[i].gene[:]
					s = temp.gene[first]
					temp.gene[first] = temp.gene[second]
					temp.gene[second] = s				
					highest = self.newpop[i].fitness(self.pop.length)
					if temp.fitness(self.pop.length) > highest :
						self.newpop[i].gene[:] = temp.gene[:]
						changed = True
					count += 1
	
	def mutation_mix (self) :
		self.mutation_random()
		self.mutation_improve()

	def swap_new (self) :
		self.pop.strings = self.newpop[:]
				



















