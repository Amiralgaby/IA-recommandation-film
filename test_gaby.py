#python test

import numpy as np
import pandas as pd

def print_list(liste):
	print('la longueur de la liste est : ',len(liste),'\n','-'*8)
	for i in liste:
		print(i)


f = open('Data/temp.dat', 'r')
# là ça fait une liste de liste
l = [ list(line.split('::')) for line in f ]

print_list(l)

#iterable = l.pop()
#l.extend(iterable)
#l.extend(iterable)

#list_iterator = l.pop() # on prend le dernier map object
#print_iterator(list_iterator) # on l'itère
