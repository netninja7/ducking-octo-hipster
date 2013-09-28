import genetic_population as gp
import genetic_operators as go
import agents, time
import sys

class ga :

	def __init__ (self) :
		# Variables
		self.num_Strings	= 30			# Defines the population size
		self.len_Strings	= 26			# Defines the length of each gene/string
		self.binary 		= False		# Selects if the string will be bits or numbers from 1..len_String
		self.Pc				= 0.80		# Defines the probability of crossover (how many strings will be selected for mating)
		self.Pm				= 0.10		# Defines the probability of mutation
		self.generations	= 10000
		self.show_gen		= 500
		self.genop			= None		# Holds the population
		self.answer			= False		# Defines if an answer has been found

	def __init__ (self, iPopSize,iLenGene,bBinary,fPc,fPm,iGen,iShowGen,sFitness) :
		# Variables
		self.num_Strings	= iPopSize		# Defines the population size
		self.len_Strings	= iLenGene		# Defines the length of each gene/string
		self.binary 		= bBinary		# Selects if the string will be bits or numbers from 1..len_String
		self.Pc				= fPc				# Defines the probability of crossover (how many strings will be selected for mating)
		self.Pm				= fPm				# Defines the probability of mutation
		self.generations	= iGen			# Defines number of generations to iterate through
		self.show_gen		= iShowGen		# Defines frequency of showing population progress
		self.genop			= None			# Holds the population
		self.answer			= False			# Defines if an answer has been found
		self.fitness		= sFitness		# DANGEROUS i know

	def create (self) :
		# create an initial population with (# strings, len of strings, if binary)
		pop =  gp.population(self.num_Strings,self.len_Strings,self.binary)
		# Once initialized gen_op will find the total sum, create the CDF, and create an intermediate generation
		self.genop = go.gen_op(pop,self.Pc,self.Pm,self.fitness)
		print "Initial Pop:"
		self.genop.pop.get_pop()

	def run (self) :
		for i in range(0, self.generations) :
			if (i + 1) % self.show_gen == 0 :
				print "generation %s" % (i+1) 
				self.genop.pop_sum()
				self.genop.pop.get_pop()
				self.genop.clear()
				#time.sleep(1)
				#raw_input('Hit enter for next 500')
			if i != self.generations - 1 :
				self.genop.run_gen()
				self.genop.next_gen()
				for string in self.genop.pop.strings :
					if string.result == 1.0 :
						print "\n\n%s Fitness:%s" % (string.gene,string.result)
						sys.exit(1)
			else :
				self.genop.clear()
				self.genop.pop_sum()
	
		print "Final Pop:"
		self.genop.pop.get_pop()
