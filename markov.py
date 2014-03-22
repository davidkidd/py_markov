#!/usr/bin/env python

'''
Simple Markov chain generator.

By default, it will load a text file and
automatically build a database, ready to
generate Markov chains.

Eg.

  from markov import Markov

  m = Markov('kingjamesbible.txt')

  print m.get_text(30)

Alternatively, add multiple text sources. The
database must be manually built prior to requesting
a chain.

  from markov import Markov

  myCorpusText = "..."
  
  m = Markov()

  m.add_text(myCorpusText)
  m.add_text(myOtherCorpusText)

  m.build()

  print m.get_text(30)

'''

from random import randint, choice
import re

class Markov():
  
  def __init__(self, filename="", build=True):
    self.database = {}
    self.words = []

    if filename:
      self.load_file(filename, build)

  def load_file(self, filename, build):
    with open(filename, 'r') as in_file:
      self.add_text(in_file.read(), build)

  def add_text(self, text, build=False):
  	self.words += self.clean_text(text)
  	if build:
  		self.build()

  def clean_text(self, text):
  	return re.sub('(http://.*|@.*|RT)','',text).split()

  def build(self):
    for a, b, c in self.get_triplet():
      if (a, b) in self.database:
        self.database[(a, b)].append(c)
      else:
        self.database[(a, b)] = [c]
  
  def get_triplet(self):
    return ((self.words[i], self.words[i+1], self.words[i+2]) for i in range (len(self.words)-2))
        
  def get_text(self, num_words):
    if self.database:
      idx = randint(0, len(self.words)-2)
      first_word = self.words[idx]
      second_word = self.words[idx+1]

      a, b = first_word, second_word

      entry = []

      for i in range(num_words):
        entry.append(a)
        try:
          a, b = b, choice(self.database[(a, b)])
        except:
          break

      return ' '.join(entry)

    else:
      print "Cannot generate new chain; database is empty."