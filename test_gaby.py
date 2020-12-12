#!/usr/bin/env python

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
	l = [ list(line.strip('\n').split('::')) for line in f ]
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


def liste_TO_dataFrame2(liste,columms):
	assert len(columms) == len(liste[0])
	colList = [ [] for _ in columms]
	for i in liste:
		for j in range(0,len(columms)):
			colList[j].append(i[j])
	d = {}
	for i in range(0,len(colList)):
		d[columms[i]] = pd.Series(colList[i])
	df = pd.DataFrame(d)
	return df


######################################
		###### Pour les ratings (test ) 
col = ['UserID','MovieID','Rating','Timestamp']

if fichierAOuvir == "Data/test_gaby.dat":
	dfRatingsTest = liste_TO_dataFrame2(l,col)
	print(dfRatingsTest)
else:
	print_list_of_list(l)


#######################################
			#### Pour les movies (test)
fichierAOuvir = 'Data/temp.dat'
try:
	# Ouverture du fichier
	f = open(fichierAOuvir, 'r')
	# là ça fait une liste de liste
	l = [ list(line.strip('\n').split('::')) for line in f ]
except Exception as e:
	print("le problème vient du fichier : ",fichierAOuvir)
	raise e


col = ['MovieID','Title','Genres']
dfMoviesTest = liste_TO_dataFrame2(l,col)
print(dfMoviesTest)


####################################
			#### Pour les users ####
fichierAOuvir = 'Data/users.dat'
try:
	# Ouverture du fichier
	f = open(fichierAOuvir, 'r')
	# là ça fait une liste de liste
	l = [ list(line.strip('\n').split('::')) for line in f ]
except Exception as e:
	print("le problème vient du fichier : ",fichierAOuvir)
	raise e


col = ['UserID','Gender','Age','Occupation','Zip-code']
dfUser = liste_TO_dataFrame2(l,col)
print(dfUser)


#######################################