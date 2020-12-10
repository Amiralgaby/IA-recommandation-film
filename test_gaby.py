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


def print_list_of_list(liste):
	for i in liste:
		print_list(i)


def liste_TO_dataFrame(liste):
	UserID = list()
	MovieID = list()
	Rating = list()
	Timestamp = list()
	for i in liste:
		# i est une liste
		UserID.append(i[0])
		MovieID.append(i[1])
		Rating.append(i[2])
		Timestamp.append(i[3])
	d = {
		'UserID': pd.Series(UserID),
		'MovieID': pd.Series(MovieID),
		'Rating' : pd.Series(Rating),
		'Timestamp' : pd.Series(Timestamp)
		}
	df = pd.DataFrame(d)
	return df


def liste_TO_dataFrame2(liste,Columms):
	assert len(Columms) == len(liste[0])
	colList = [ [] for _ in Columms] # Merci à quelqu'un du serv Nan
	for i in liste:
		for j in range(0,len(Columms)):
			colList[j].append(i[j])
	d = {}
	for i in range(0,len(colList)):
		d[Columms[i]] = pd.Series(colList[i])
	df = pd.DataFrame(d)
	return df

col = ['UserID','MovieID','Rating','Timestamp']
#liste_TO_dataFrame2(l,col)

print('la longueur de la liste est : ',len(l),'\n','-'*8)
print_list(l)

if fichierAOuvir == "Data/test_gaby.dat":
	df = liste_TO_dataFrame2(l,col)
	print(df)
else:
	print_list_of_list(l)

#data = ["foo", "foofoo", "foofoofoo"]
#index = ["1er element", "2eme element", "3eme element"]
#s = pd.Series(data, index=index)