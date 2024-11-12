# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 12:24:01 2024

@author: USER
"""

"""



"""

print("1-\n   Écrivez un programme Python pour lire ➡️ un fichier texte entier.")

f = open("fichier.txt", 'r', encoding='utf-8')


f.read() 

print("2\n   Écrivez un programme Python pour lire les n premières lignes d'un fichier.")

p1 = open("fichier.txt", 'r', encoding='utf-8')

p1.read(n)


print("3\n   Écrivez un programme Python pour lire les n dernières lignes d'un fichier.")
p2 = open("fichier.txt", 'r', encoding='utf-8')

p2.read(-n)

print("4\n   Écrivez un programme Python qui prend un fichier texte en entrée et renvoie le nombre de mots de ce fichier texte.")

with open("test.txt", 'w', encoding='utf-8') as f:

   f.write("Le pays doit son nom à l'expression 'Sunuu gaal' car bordé par la mer et aussi par le fleuve Sénégal qui le borde à l'est et au nord et qui prend sa source dans le Fouta-Djalon en Guinée. Le climat est tropical et sec avec deux saisons : la saison sèche et la saison des pluies.\n")


print("2\n   (Bonus) Écrivez un programme Python pour lire les n dernières lignes d'un fichier.")
p3 = open("fichier.txt", 'r', encoding='utf-8')

p3.read(-n)