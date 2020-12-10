#python test

import numpy as np
import pandas as pd

def print_iterator(it):
	print('la longueur de la liste est : ',len(it))
	for x in it:
		print(x)

f = open('Data/temp.dat', 'r')
# là ça fait une liste
l = [ list(line.split('::')) for line in f ]

print(l)
print('-'*8)
#list_iterator = l.pop() # on prend le dernier map object
#print_iterator(list_iterator) # on l'itère
