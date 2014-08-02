#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sans titre.py
#  
#  
print ('Entrez la note obtenue'),
n=input()
print('Entrez sur quel total la note à été obtenu'),
a=input()
c=100
note =''
p=n/a*c
if p >= 80 :
	note='A'
	print ("L'appréciation de l'éléve est "),note
	
elif p > 80 and p >= 60 :
	note = 'B'
	print ("L'appréciation de l'éléve est "),note

elif p > 60 and p >= 50 :
	note = 'C'
	print ("L'appréciation de l'éléve est "),note
	
elif p > 50 and p >= 40 :
	note = 'D'
	print ("L'appréciation de l'éléve est "),note
	
else :
	note = 'E'
	print ("L'appréciation de l'éléve est "),note
