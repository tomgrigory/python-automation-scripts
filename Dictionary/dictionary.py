words = set()


def check(word):
	if word.lower() in words:
		print("Yeah it is in the dictionary")
		return True
	else:
		print("Sorry it is not in the dictionary")
	    	

def load(dictionary):
	file = open(dictionary , "r")
	for line in file:
		words.add(line.rstrip("\n"))
	file.close()
	return True	


def size():
	return len(words)


def unload():
	return True

load("large")	
check("zeffujufa")

