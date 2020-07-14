# Write the function eggCartons(eggs) that takes 
# a non-negative integer number of eggs, and returns 
# the smallest integer number of cartons required to hold 
# that many eggs, where a carton may hold up to 12 eggs


def fun_eggcartons(eggs):
	# your code goes here
	n = eggs /12
	s = str(n)
	l = str.split('.')
	if (int(l[1]) > 0):
		return int(l[0]) + 1
	else:
		return int(l[0])


