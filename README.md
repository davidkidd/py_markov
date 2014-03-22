py_markov
=========

The smallest, sanest usable Markov chain generator I could think of.

Try loading a file into a Markov object, then generate 30 words of new text:

	from markov import Markov
		  
	m = Markov('kingjamesbible.txt')
		  
	print m.get_text(30)

Alternatively, add multiple text sources:
	
	from markov import Markov

	myCorpusText = "..."
  
	m = Markov()

	m.add_text(myCorpusText)
	m.add_text(myOtherCorpusText)

	m.build()

	print m.get_text(30)
