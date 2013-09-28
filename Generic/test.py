from crypto_fitness import *
import agents

temp = agents.agent()
temp.load_gene([22, 10, 16, 25, 20, 18, 2, 26, 11, 3, 19, 8, 24, 4, 23, 7, 14, 1, 9, 12, 15, 5, 17, 13, 6, 21])

print fitness(temp ,26)

fhCrypt = open("crypto.txt")
newAlpha = convert(temp.gene)
print flip(fhCrypt.readline(),newAlpha)

