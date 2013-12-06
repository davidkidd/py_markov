#!/usr/bin/env python

'''
Simple Markov chain generator.

Eg.

  from markov import Markov

  m = Markov('kingjamesbible.txt')

  print m.get_text(30)

Alternatively, load text directly into an empty Markov object

  from markov import Markov

  myCorpusText = "..."
  
  m = Markov()

  m.load_text(myCorpusText)

  print m.get_text(30)

'''

from random import randint, choice
import re

class Markov():
  
  def __init__(self, filename=""):
    self.database = {}
    self.words = []

    if filename:
      self.load_file(filename)

  def load_file(self, filename):
    with open(filename, 'r') as in_file:
      self.load_text(in_file.read())
    
  def load_text(self, text):
    self.words = re.sub('(http://.*|@.*|RT)','',text).split()
    self.build_database()

  def build_database(self):
    for a, b, c in self.get_triplet():
      if (a, b) in self.database:
        self.database[(a, b)].append(c)
      else:
        self.database[(a, b)] = [c]
  
  def get_triplet(self):
    return ((self.words[i], self.words[i+1], self.words[i+2]) for i in range (len(self.words)-2))
        
  def get_text(self, num_words):
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