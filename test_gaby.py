#python test

import pandas as pd

def function(file):
	f = open(file, 'r')
	fic = f.read()
	f.close
	return fic

def print_iterator(it):
    for x in it:
        print(x, end='\n')

f = open('movies.dat', 'r')
# là ça fait une liste
l = [ map(str,line.split('::')) for line in f ]

map_iterator = l.pop() # on prend le dernier map object
print_iterator(map_iterator) # on l'itère
