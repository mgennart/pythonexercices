#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sansfonction

def surfCercle (r):
	aire = (r**2)*3.1416
	return aire

print surfCercle (20)

def volBoite (lo,la,ha):
	volume = lo*la*ha
	return volume

print volBoite (53,22,58)

def chiffremax (n1,n2,n3):
	if n1 > n2 and n1>n3:
		return n1
	elif n2 > n1 and n2 >n3:
		return n2
	else:
		return n3

print chiffremax (1,4,3)

def comptecar (ca,ch):
	i,nc=0,0
	while i < len(ch):
		if ch[i] == ca:
			nc=nc+1
		i=i+1
	return nc
	
print comptecar ('e','phrase de test')

