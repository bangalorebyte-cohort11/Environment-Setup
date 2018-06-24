from __future__ import print_function
def divby_7():
	to_num =[]
	for i in range(2000, 3200):
		if i % 7 == 0:
			digit = [str(d) for d in str(i)]
			if digit[-1] != '0' and digit[-1] != '5':
				to_num = "".join(digit)
			print (int(to_num), end=", ")

divby_7()