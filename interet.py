#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  exercice 4 interet
#  

compteur = 1
capital = 100
taux = 4.3
interets = 0
interetsCumules = 0

while (compteur<21):
    capital = capital + interets
    interets =  capital*taux/100
    interetsCumules = interetsCumules + interets
    
    print "annee", compteur, "= capital", capital, "|| interets =", interets
    print "interets cumules =", interetsCumules

    compteur += 1

print "somme totale des interets cumules =", interetsCumules
