import TSP_lookup as tsp
import math

DEBUG = False

class agent :

	def __init__ (self) :
		self.gene = []
		self.distance = 0.0
		self.result = 0.0
		self.value = 0
		self.rank = 0
		self.replicate = False
		
	def fitness (self, count) :
		self.distance = 0.0
		self.result = 0.0
		a = []
		b = []
		for i in range(count) :
			if i == count - 1 : # at the last city
				a = tsp.get_xy(self.gene[i])
				b = tsp.get_xy(self.gene[0]) # loop back to first city
			else :
				a = tsp.get_xy(self.gene[i])
				b = tsp.get_xy(self.gene[i+1])
			self.distance += math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) #euclidian distance function
		
		self.result = 10 / self.distance
		return self.result
		
	def load_gene (self, gene) :
		self.gene = gene
	
	