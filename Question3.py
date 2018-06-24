from __future__ import print_function

def diction(num):
	dicti = {}
	for i in num:
		dicti[i] = i*i 
	print (dicti, end=", ")


x = [1,3,8,9,4]
diction(x)