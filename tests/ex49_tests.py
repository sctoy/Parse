from nose.tools import *
from ex49 import parser
from ex49 import lexicon


def test_directions():
	assert_equal(lexicon.scan("North"),[('direction', 'north')])
	result = lexicon.scan("north south east")
	assert_equal(result, [('direction', 'north'),
						  ('direction', 'south'),
						  ('direction', 'east')])
						  
def test_verbs():
	assert_equal(lexicon.scan("go"),[('verbs', 'go')])
	result = lexicon.scan("go kill eat")
	assert_equal(result, [('verbs', 'go'),
						  ('verbs', 'kill'),
						  ('verbs', 'eat')])
						  
def test_stops():
	assert_equal(lexicon.scan("the"), [('stop', 'the')])
	result = lexicon.scan("the in of")
	assert_equal(result, [('stop', 'the'),
						  ('stop', 'in'),
						  ('stop', 'of')])
						  
def test_nouns():
	assert_equals(lexicon.scan("door"), [('nouns', 'door')])
	result = lexicon.scan("door bear princess")
	assert_equals(result, [('nouns', 'door'),
						   ('nouns', 'bear'),
						   ('nouns', 'princess')])
						   
def test_numbers():
	assert_equals(lexicon.scan("1234"), [('number', 1234)])
	result = lexicon.scan("1234 4321 8765")
	assert_equals(result, [('number', 1234),
						   ('number', 4321),
						   ('number', 8765)])
						   
def test_errors():
	assert_equals(lexicon.scan("qwerty"), [('error', 'qwerty')])
	result = lexicon.scan("qwerty ytrewq asdfg")
	assert_equals(result, [('error', 'qwerty'),
							('error', 'ytrewq'),
							('error', 'asdfg')])


def test_peek():
	assert_equal(parser.peek([('stop', 'the')]),('stop'))
	assert_equal(parser.peek([('nouns', 'bear')]),('nouns'))
	assert_equal(parser.peek([('verbs', 'kill')]),('verbs'))
	assert_equal(parser.peek([('directions', 'north')]),('directions'))
	assert_equal(parser.peek([]),(None))	

def test_match():
	assert_equal(parser.match([('nouns', 'bear'), ('stop', 'the')], 'nouns'),
								('nouns', 'bear'))
	assert_equal(parser.match([('nouns', 'bear'), ('stop', 'the')], 'verbs'),
								(None))
	assert_equal(parser.match([],''),(None))	


def test_parse_verb():
	assert_equal(parser.parse_verb([('verbs', 'kill'), ('stop', 'the')]),
									 ('verbs', 'kill'))
	# Need to figure out syntax for errors
	# assert_raises(ParserError, parser.parse_verb, [('stop', 'the')])
	

def test_parse_object():
	assert_equal(parser.parse_object([('nouns', 'bear'), ('stop', 'the')]),
		('nouns', 'bear'))
	assert_equal(parser.parse_object([('direction', 'north'),
		('stop', 'the')]), ('direction', 'north'))
	# Need ParserError check here
	

# This one needs some work. The looping nature of this is method is tricky
#def test_parse_subject():
#	assert_equal(parser.parse_subject([('verbs', 'kill'), ('nouns', 'bear')],
#		('nouns', 'cabinet')), (cabinet, kill, bear))
	

# Skip has no return. How do I test?
#def test_skip():
	
