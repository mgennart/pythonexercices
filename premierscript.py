#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Premier essai de script Python
#petit programme simple affichant une suite de Fibonnaci, càd une suite de nombre
#dont chaque terme est égal à la somme des deux précédents.

a,b,c=1,1,1 	#a &b servent au calcul des termes successifs
				# c est un simple compteur
print 1			#affichage du premier terme
while c<15:		#nous afficherons 15 termes au total
	a,b,c =b, a+b, c+1
	print b		

