#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercice 1,2 contient e

# Recherche d'un caractère particulier dans une chaîne

# Chaîne fournie au départ :
ch = "Monty python flying circus"
# Caractère à rechercher :
cr = "e"
# Recherche proprement dite :
lc = len(ch)    # nombre de caractères à tester
i = 0           # indice du caractère en cours d'examen
t = 0           # "drapeau" à lever si le caractère recherché est présent 
while i < lc:
    if ch[i] == cr:
        t = 1
    i = i + 1    
# Affichage :
print "Le caractère", cr,
if t == 1:
    print "est présent",
else:
    print "est inrouvable",
print "dans la chaîne", ch

print "comptage de e"

ch="ceci contient la lettre e"
cr="e"
lc=len(ch)
i=0
t=0
a=0
while i<lc:
	if ch[i] == cr:
		t=1
		a=a+1
	i = i+1
 
print "le caractére",cr,
if t==1:
	print "est présent",a,"fois"
else:
	print"est instrouvable",
print"dans la chaine",ch
		
