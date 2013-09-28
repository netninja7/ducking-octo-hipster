import math
import TSP_lookup as tsp


def fitness (string, count) :
	distance = 0.0
	string.result = 0.0
	a = []
	b = []
	for i in range(count) :
		if i == count - 1 : # at the last city
			a = tsp.get_xy(string.gene[i])
			b = tsp.get_xy(string.gene[0]) # loop back to first city
		else :
			a = tsp.get_xy(string.gene[i])
			b = tsp.get_xy(string.gene[i+1])
		distance += math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)) #euclidian distance function
	
	string.result = 10 / distance
	return string.result
		
