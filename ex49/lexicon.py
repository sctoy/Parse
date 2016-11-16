# Exercise from Chapter 48 in "Python The Hard Way"
# Copied here and altered to work on Chapter 49 which calls on this module


# This is a module designed to create lexicon lists that will be imported
direction = ['north', 'south', 'east', 'west', 'down', 'up',
			 'left', 'right', 'back']
verbs = ['go', 'stop', 'kill', 'eat']
stop = ['the', 'in', 'of', 'from', 'at', 'it']
nouns = ['door', 'bear', 'princess', 'cabinet']
lists = {'direction': direction, 'verbs': verbs, 'stop': stop, 'nouns': nouns}

def scan(sentence):
	sentence = sentence.lower()
	words = sentence.split()
	result = [] # changed from result in ex48 to work with ex49 code
	
	for word in words:
		found = False
		for key,value in lists.items():
			if word in value:
				result.append((key,word))
				found = True # Way to skip over the 'if not found' below
				break
		if not found:
			try:
				word = int(word) # int(word) throws error if word not an int
				# this also turns the string into an integer so need to test
				# integer i.e. 1234 not string i.e. '1234'
				result.append(('number', word))
			except ValueError:
				result.append(('error', word))

	return result

# Commented out the code below which I used to test the code above
# print "Give me a sentence:"
# sentence = raw_input()
# result_list = scan(sentence)
# print result_list
# for r in result_list:
# 	print r	

# Testing sentence below for easy copy and paste
# North south Go stop The in Door bear 1234 Steven 4321 Colleen