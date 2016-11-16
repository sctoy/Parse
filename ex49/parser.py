# Exercise 49 from "Learn Python the Hard Way"

import lexicon


# This is important for defining ParserErrors below so that they work
class ParserError(Exception):
	pass
	

# To be honest I do not truly understand what this is ultimately trying
# to accomplish. Theoretically it allows a wider range of inputs into the
# a game but it appears incredibly clunky. Perhaps that is because this needs
# to be pretty simple as an exercise but it isn't very intuitive.	
class Sentence(object):

	def __init__(self, subject, verb, object):
		# remember we take ('noun', 'princess') tuples and convert them
		self.subject = subject[1]
		self.verb = verb[1]
		self.object = object[1]
		
		print self.subject, self.verb, self.object


# This function/method allows to look at the first word_type in a list	
def peek(word_list):
	if word_list: # if there is something in word_list resolves to True
		word = word_list[0]
		return word[0] # [0] b/c word contains tuples and we want the first var
	else:
		return None
		

# This function pops off the first word, reducing word_list and returning
# the word tuple to whatever called it.
def match(word_list, expecting):
	if word_list:
		word = word_list.pop(0)
		
		if word[0] == expecting:
			return word
		else:
			return None
	else:
		return None
		

# Method to skip over all words of certain type. Used only for 'stop'.
def skip(word_list, word_type):
	while peek(word_list) == word_type:
		match(word_list, word_type)
		

# Method checks word_type of item in list, to see if the first non-'stop'
# is a verb. If yes uses match to pop it off. If no throws an error.
def parse_verb(word_list):
	skip(word_list, 'stop')
	
	if peek(word_list) == 'verbs':
		return match(word_list, 'verbs')
	else:
		raise ParserError("Expected a verb next.")
		

# Method checks word_type of item in list, to see if the first non-'stop'
# is a noun or direction. If yes uses match to pop it off. No throws error.
def parse_object(word_list):
	skip(word_list, 'stop')
	next = peek(word_list)
	
	if next == 'nouns':
		return match(word_list, 'nouns')
	if next == 'direction':
		return match(word_list, 'direction')
	else:
		raise ParserError("Expected a noun or direction next.")
		

# If the first non-'stop' word is a noun it is assumed to be the subject.
# The opening noun tuple is passed to this method via parse_sentence.
# If the  first non-'stop' word is a verb it is assumed player is the subject.
# A default ('noun', 'player') is passed to this method via parse_sentence.
# The resulting subj, verb, obj is passed to class Sentence.	
def parse_subject(word_list, subj):
	verb = parse_verb(word_list)
	obj = parse_object(word_list)
	
	return Sentence(subj, verb, obj)
	

# Figures out whether the first non-'stop' word in the initial word_list
# is a noun or verb and throws an error if neither as defined in lists.
def parse_sentence(word_list):
	skip(word_list, 'stop')
	
	start = peek(word_list)
	
	if start == 'nouns':
		subj = match(word_list, 'nouns')
		return parse_subject(word_list, subj)
	elif start == 'verbs':
		# assume the subject is the player then
		return parse_subject(word_list, ('nouns', 'player'))
	else:
		raise ParserError("Must start with sbj, obj, or vrb not: %s" % start)


# Various instructions for testing code.
# print "Give me a sentence:"
# sentence = raw_input()
# word_list = lexicon.scan(sentence)
# parse_sentence(word_list)

# Other tests. Requires print statements within methods
# print word_list	
# peek(word_list)
# match(word_list, 'nouns')
# skip(word_list, 'nouns')
# parse_verb(word_list)
# parse_object(word_list)

# Basic test sentence
# The princess eat bear



