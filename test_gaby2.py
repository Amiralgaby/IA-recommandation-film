#!/usr/bin/env python
import sys
import pandas as pd

if len(sys.argv) < 2:
	print("usage ",sys.argv[0]," <nom du fichier>")
	exit()
fichierAOuvir = sys.argv[1]
print('Ouverture du fichier : ',fichierAOuvir)

df = pd.read_csv("Data/temp.dat", sep='::', names=["UserID", "MovieID", "Rating", "Timestamp"])
print(df)
# RATING.DAT

#  | UserID | MovieID | Rating | Timestamp
# 1
# 2
# 3
# 4
# 5
# 6