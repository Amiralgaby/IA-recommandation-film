#python test

import numpy as np
import pandas as pd
import sys

if len(sys.argv) < 2:
	fichierAOuvir = 'Data/temp.dat'
else :
	fichierAOuvir = sys.argv[1]

print('Ouverture du fichier : ',fichierAOuvir)

try:
	# Ouverture du fichier
	f = open(fichierAOuvir, 'r')
	# là ça fait une liste de liste
	l = [ list(line.split('::')) for line in f ]
except Exception as e:
	print("le problème vient du fichier : ",fichierAOuvir)
	raise e
else:
	print("Réussi")


def print_list(liste):
	for i in liste:
		print(i)


def liste_to_dataFrame(liste):
	for i in liste:
		print_list(i)

print('la longueur de la liste est : ',len(l),'\n','-'*8)
print_list(l)

liste_to_dataFrame(l)

#data = ["foo", "foofoo", "foofoofoo"]
#index = ["1er element", "2eme element", "3eme element"]
#s = pd.Series(data, index=index)