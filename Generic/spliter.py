fh = open("long.txt")

for line in fh :
	length = len(line)-1
	if length == 1 :
		hand = open("1.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 2 :
		hand = open("2.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 3 :
		hand = open("3.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 4 :
		hand = open("4.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 5 :
		hand = open("5.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 6 :
		hand = open("6.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 7 :
		hand = open("7.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 8 :
		hand = open("8.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 9 :
		hand = open("9.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 10 :
		hand = open("10.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 11 :
		hand = open("11.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 12 :
		hand = open("12.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 13 :
		hand = open("13.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 14 :
		hand = open("14.txt", 'a')
		hand.write(line)
		hand.close()
	elif length == 15 :
		hand = open("15.txt", 'a')
		hand.write(line)
		hand.close()
	else :
		hand = open("long2.txt", 'a')
		hand.write(line)
		hand.close()
print "Done!!!"
