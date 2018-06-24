from __future__ import print_function

def diction(num):
	dicti = {}
	for i in range(1, num+1):
		dicti[i] = i*i 
	print (dicti, end=", ")


x = 8
diction(x)