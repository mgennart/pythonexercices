#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# # Insertion d'un caractère d'espacement dans une chaîne

# Chaîne fournie au départ :
ch = "Gaston"
# Caractère à insérer :
cr = "*"
# Le nombre de caractères à insérer est inférieur d'une unité au
# nombre de caractères de la chaîne. On traitera donc celle-ci à
# partir de son second caractère (en omettant le premier).
lc = len(ch)    # nombre de caractères total
i = 1           # indice du premier caractère à examiner (le second, en fait)
nch = ch[0]     # nouvelle chaîne à construire (contient déjà le premier car.)
while i < lc:
    nch = nch + cr + ch[i]
    i = i + 1    
# Affichage :
print nch


print "inverser chaine"
# Inversion d'une chaîne de caractères

# Chaîne fournie au départ :
ch = "zorglub"
lc = len(ch)    # nombre de caractères total
i = lc - 1      # le traitement commencera à partir du dernier caractère
nch = ""        # nouvelle chaîne à construire (vide au départ)
while i >= 0:
    nch = nch + ch[i]
    i = i - 1    
# Affichage :
print nch  

print "palindrome"

ch="revoir"
lc=len(ch)
i= lc-1
nch =""
while i>=0:
	nch = nch +ch[i]
	i=i-1

if ch==nch:
	print "ceci est un palindrome"
else:
	print "ceci n'est pas un palindrome"


