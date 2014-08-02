#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sans titre.py
#  
# 
# Traitement de nombres entiers compris entre deux limites

print "Veuillez entrer la limite inférieure :",
a = input()
print "Veuillez entrer la limite supérieure :",
b = input()
s = 0                   # somme recherchée (nulle au départ)
# Parcours de la série des nombres compris entre a et b :
n = a                   # nombre en cours de traitement
while n <= b:
    if n % 3 ==0 and n % 5 ==0:      # variante : 'or' au lieu de 'and'
        s = s + n
    n = n + 1

print "La somme recherchée vaut", s


print "entrez l'année "
a = input ()
if ( a%4==0 ) or (a %100==0):
	print "c'est une année bissextile"
else:
	print "ce n'est pas une année bissextille"

	
print "entrez votre nom",
nom = raw_input()
print "entrez votre sexe M ou F",
sexe = raw_input()
f="f"
if sexe==f:
	print "Chère Mademoiselle ",nom
else:
	print"Cher Monsieur ",nom
