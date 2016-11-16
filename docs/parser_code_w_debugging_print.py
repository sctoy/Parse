import lexicon

class ParserError(Exception):
	pass
	
	
class Sentence(object):

	def __init__(self, subject, verb, object):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]
		print "class Sentence was called with: %s, %s and %s" % (self.subject,
			self.verb, self.object)


# ++++++++++++++++++++++++++++++
# Here for the sole purpose of getting nosetests working
def adding(a, b):
	print a + b
	return a + b
	
# Here for the sole purpose of getting nosetests working
def add_tuples(t):
	new_list = []
	for x in t:
		new_list.append(x[0] + x[1])
	print new_list
	return new_list
# ++++++++++++++++++++++++++++++

		
def peek(word_list):
	if word_list: # if there is something in word_list resolves to True
		word = word_list[0]
		return word[0] # [0] b/c word contains tuples and we want the first var
	else:
		return None
		

def match(word_list, expecting):
	print "match received %s and %s." % (word_list, expecting)
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expecting:
			print "match == expecting and returned:", word
			return word
		else:
			print "word[0] != expecting and returned 'None'"
			return None
	else:
		print "match was False (no word_list) and returned: 'None'"
		return None
		

def skip(word_list, word_type):
	print "skip received %s and %s." % (word_list, word_type)
	while peek(word_list) == word_type:
		match(word_list, word_type)
		
		
def parse_verb(word_list):
	print "parse_verb received %s." % word_list
	skip(word_list, 'stop')
	
	if peek(word_list) == 'verbs':
		print "parse_verb's peek call True and returns 'match(word_list, 'verb')'"  
		return match(word_list, 'verbs')
	else:
		raise ParserError("Expected a verb next.")
		
		
def parse_object(word_list):
	print "parse_object received %s." % word_list
	skip(word_list, 'stop')
	next = peek(word_list)
	
	if next == 'nouns':
		return match(word_list, 'nouns')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")
		
		
def parse_subject(word_list, subj):
	print "parse_subject received %s and %s." % (word_list, subj)
	verb = parse_verb(word_list)
	obj = parse_object(word_list)
	
	return Sentence(subj, verb, obj)
	
	
def parse_sentence(word_list):
	print "parse_sentence received %s." % word_list
	skip(word_list, 'stop')
	
	start = peek(word_list)
	
	if start == 'nouns':
		subj = match(word_list, 'nouns')
		print "parse_sentence 'start == 'nouns'' True."
		return parse_subject(word_list, subj)
	elif start == 'verbs':
		# assume the subject is the player then
		print "parse_sentence 'start == 'verbs'' True."
		return parse_subject(word_list, ('nouns', 'player'))
	else:
		raise ParserError("Must start with sbj, obj, or vrb not: %s" % start)

adding(3, 4)
z = [(1, 9), (1, 1), (1, 2)]
add_tuples(z)
# print "Give me a sentence:"
# sentence = raw_input()
# word_list = lexicon.scan(sentence)
# print word_list	
# peek(word_list)
# match(word_list, 'nouns')
# skip(word_list, 'nouns')
# parse_verb(word_list)
# parse_object(word_list)
# parse_sentence(word_list)


# Princess eat bear
