
def fitness(string, length) :
	strSum = 0.0
	newAlpha = convert(string.gene)
	fhCrypt = open("crypto.txt")
	flippedCrypt = ""
	flippedCrypt = flip(fhCrypt.readline(),newAlpha)
	flippedCrypt = flippedCrypt.split()
	for word in flippedCrypt :
		#print "Word: %s" % word
		if len(word) == 1 :
			fhDict = open("1.txt")
		elif len(word) == 2 :
			fhDict = open("2.txt")
		elif len(word) == 3 :
			fhDict = open("3.txt")
		elif len(word) == 4 :
			fhDict = open("4.txt")
		elif len(word) == 5 :
			fhDict = open("5.txt")
		elif len(word) == 6 :
			fhDict = open("6.txt")
		elif len(word) == 7 :
			fhDict = open("7.txt")
		elif len(word) == 8 :
			fhDict = open("8.txt")
		elif len(word) == 9 :
			fhDict = open("9.txt")
		elif len(word) == 10 :
			fhDict = open("10.txt")
		elif len(word) == 11 :
			fhDict = open("11.txt")
		elif len(word) == 12 :
			fhDict = open("12.txt")
		elif len(word) == 13 :
			fhDict = open("13.txt")
		elif len(word) == 14 :
			fhDict = open("14.txt")
		elif len(word) == 15 :
			fhDict = open("15.txt")
		else :
			fhDict = open("long.txt")
		
		for line in fhDict :
			count = 0.0
			highest = 0.0
			if len(line)-1 == len(word) :
				for n in range(0,len(word)) :
					if line[n].upper() == word[n] :
						count += 1
			highest = count / len(word)
			if highest == 1 :
				print "Match: %s" % line
				break
				
		strSum += highest
				
		fhDict.close()
	
	string.result = strSum / len(flippedCrypt)
	return string.result

def flip (string, alpha) :
	temp = []
	for i in range(0,len(string)) :
		if string[i] == "a" or string[i] == "A" :
			temp.append(alpha[0])
		elif string[i] == "b" or string[i] == "B" :
			temp.append(alpha[1])
		elif string[i] == "c" or string[i] == "C" :
			temp.append(alpha[2])
		elif string[i] == "d" or string[i] == "D" :
			temp.append(alpha[3])
		elif string[i] == "e" or string[i] == "E" :
			temp.append(alpha[4])
		elif string[i] == "f" or string[i] == "F" :
			temp.append(alpha[5])
		elif string[i] == "g" or string[i] == "G" :
			temp.append(alpha[6])
		elif string[i] == "h" or string[i] == "H" :
			temp.append(alpha[7])
		elif string[i] == "i" or string[i] == "I" :
			temp.append(alpha[8])
		elif string[i] == "j" or string[i] == "J" :
			temp.append(alpha[9])
		elif string[i] == "k" or string[i] == "K" :
			temp.append(alpha[10])
		elif string[i] == "l" or string[i] == "L" :
			temp.append(alpha[11])
		elif string[i] == "m" or string[i] == "M" :
			temp.append(alpha[12])
		elif string[i] == "n" or string[i] == "N" :
			temp.append(alpha[13])
		elif string[i] == "o" or string[i] == "O" :
			temp.append(alpha[14])
		elif string[i] == "p" or string[i] == "P" :
			temp.append(alpha[15])
		elif string[i] == "q" or string[i] == "Q" :
			temp.append(alpha[16])
		elif string[i] == "r" or string[i] == "R" :
			temp.append(alpha[17])
		elif string[i] == "s" or string[i] == "S" :
			temp.append(alpha[18])
		elif string[i] == "t" or string[i] == "T" :
			temp.append(alpha[19])
		elif string[i] == "u" or string[i] == "U" :
			temp.append(alpha[20])
		elif string[i] == "v" or string[i] == "V" :
			temp.append(alpha[21])
		elif string[i] == "w" or string[i] == "W" :
			temp.append(alpha[22])
		elif string[i] == "x" or string[i] == "X" :
			temp.append(alpha[23])
		elif string[i] == "y" or string[i] == "Y" :
			temp.append(alpha[24])
		elif string[i] == "z" or string[i] == "Z" :
			temp.append(alpha[25])
		else :
			temp.append(string[i])
	return ''.join(temp)

	
def convert (string) :
	newAlpha = []
	for i in string :
		if i == 1 :
			newAlpha.append("A")
		elif i == 2 :
			newAlpha.append("B")
		elif i == 3 :
			newAlpha.append("C")
		elif i == 4 :
			newAlpha.append("D")
		elif i == 5 :
			newAlpha.append("E")
		elif i == 6 :
			newAlpha.append("F")
		elif i == 7 :
			newAlpha.append("G")
		elif i == 8 :
			newAlpha.append("H")
		elif i == 9 :
			newAlpha.append("I")
		elif i == 10 :
			newAlpha.append("J")
		elif i == 11 :
			newAlpha.append("K")
		elif i == 12 :
			newAlpha.append("L")
		elif i == 13 :
			newAlpha.append("M")
		elif i == 14 :
			newAlpha.append("N")
		elif i == 15 :
			newAlpha.append("O")
		elif i == 16 :
			newAlpha.append("P")
		elif i == 17 :
			newAlpha.append("Q")
		elif i == 18 :
			newAlpha.append("R")
		elif i == 19 :
			newAlpha.append("S")
		elif i == 20 :
			newAlpha.append("T")
		elif i == 21 :
			newAlpha.append("U")
		elif i == 22 :
			newAlpha.append("V")
		elif i == 23 :
			newAlpha.append("W")
		elif i == 24 :
			newAlpha.append("X")
		elif i == 25 :
			newAlpha.append("Y")
		elif i == 26 :
			newAlpha.append("Z")
	return newAlpha










