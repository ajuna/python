import sys
print"Enter a input file"
inputfile=input()
def word_count(inputfile):
  dict1={}
  for line in inputfile:
	words=line.split()
	for word in words:
	  word=word.lower()
	  print"list of words", word
	  if not word in dict1:
		dict1[word]=1
	  else:
		dict1[word]=dict1[word]+1
  return word_count

def print_words(inputfile):
  dict1=word_count(inputfile)
  words=sorted(dict1.keys())
  for word in words:
	print word,dict1[word]
  return print_words


