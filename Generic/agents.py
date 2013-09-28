import math

DEBUG = False

class agent :

	def __init__ (self) :
		self.gene = []
		self.result = 0.0
		self.value = 0
		self.rank = 0
		self.replicate = False
		
	def load_gene (self, gene) :
		self.gene = gene
	
	
