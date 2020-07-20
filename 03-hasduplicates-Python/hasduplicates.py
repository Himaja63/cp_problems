# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

from itertools import chain
def hasduplicates(L):
	# Your code goes here
	flag = 0
	l = list(chain.from_iterable(L))
	for i in range(len(l)):
		for j in range(len(l)):
			if (i != j):
				if (l[i] == l[j]):
					flag = 1
					break
	if flag == 1:
		return True
	else:
		return False