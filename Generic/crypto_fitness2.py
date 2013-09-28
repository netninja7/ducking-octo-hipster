import random
import math

def fitness(string, length) :
	count = 0.0	
	for i in range(0,length) :
		#if i == length-1 :
		#	pass
		#elif string.gene[i] == string.gene[i+1]-1 :
		#	count += 1
		#	if i == length-2 :
		#		pass
		#	elif string.gene[i] == string.gene[i+2]-2 :
		#		count +=1
		if string.gene[i]-1 == i :
			count +=1

	string.result = count / 26
	return string.result


