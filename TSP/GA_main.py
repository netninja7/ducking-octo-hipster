import TSP_lookup as tsp
import genetic_population as gp
import genetic_operators as go
import agents, time

# Variables
num_Strings	= 30		# Defines the population size
len_Strings	= 10		# Defines the length of each gene/string
binary 		= False		# Selects if the string will be bits or numbers from 1..len_String
Pc		= 0.75		# Defines the probability of crossover (how many strings will be selected for mating)
Pm		= 0.0125	# Defines the probability of mutation
generations	= 5000

# create an initial population with (# strings, len of strings, if binary)
pop =  gp.population(num_Strings,len_Strings,binary)

#pop.get_pop()
#print "Post"
# Once initialized gen_op will find the total sum, create the CDF, and create an intermediate generation
genop = go.gen_op(pop,Pc,Pm)
print "Initial Pop:"
genop.pop.get_pop()


for i in range(0, generations) :
	if (i + 1) % 500 == 0 :
		print "generation %s" % (i+1) 
		genop.pop_sum()
		genop.pop.get_pop()
		genop.clear()
		#time.sleep(1)
		# raw_input('Hit enter for next 500')
	if i != generations - 1 :
		genop.run_gen()
		genop.next_gen()
	else :
		genop.clear()
		genop.pop_sum()

print "Final Pop:"
genop.pop.get_pop()
