#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercice 1 liste

t1 = [31,28,31,30,31,30,31,31,30,31,30,31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
      'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3=[]
lct2=len(t2)
b=0
while b<lct2:
	t3.append(t2[b])
	t3.append(t1[b])
	b=b+1
print t3

	
# Affichage des éléments d'une liste

# Liste fournie au départ :
t2 = ['Janvier','Février','Mars','Avril','Mai','Juin',
      'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
# Affichage :
i = 0
while i < len(t2):
    print t2[i],
    i = i + 1
    
print " Ressortir le plus grand nombre"

ts=[12,24,52,46]
i=0
a=0
while i<len(ts):
	if ts[i]>a:
		a=ts[i]
	i=i+1
print  "Le plus grand élément de cette liste a la valeur", a

print"liste pair et impaire"

ts=[12,24,52,46,8,4,2,9,5,7,77,55,33]
paire=[]
impaire=[]
i=0
while i < len(ts):
	if ts[i]%2==0:
		paire.append(ts[i])
	else:
		impaire.append(ts[i])
	i=i+1
print "liste des paire est",paire,"la liste des impaire est",impaire



print "liste de 6 caractéres"

ts=['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
a=[]
b=[]
i=0
while i<len(ts):
	if len(ts[i])< 6:
		a.append(ts[i])
	else:
		b.append(ts[i])
	i=i+1
print "liste des noms de moins de 6 caractére ",a,"la liste des noms de 6 et plus 6 caractéres",b

	

















