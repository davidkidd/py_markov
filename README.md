py_markov
=========

The smallest, sanest usable Markov chain generator I could think of.

Try loading a file into a Markov object, then generate 30 words of new text:

	from markov import Markov
		  
	m = Markov('kingjamesbible.txt')
		  
	print m.get_text(30)

Alternatively, load text directly into an empty Markov object:
	
	from markov import Markov
	
	myCorpusText = "..."
	  
	m = Markov()
	
	m.load_text(myCorpusText)
	
	print m.get_text(30)
