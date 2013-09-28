import agents

test = agents.agent()

for i in range(1,10) :
	test.gene.append(i)

test.fitness(10)

