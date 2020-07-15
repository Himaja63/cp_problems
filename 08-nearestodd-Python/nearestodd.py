# Write the function nearestOdd(n) that takes an float n, 
# and returns as an int value the nearest odd number to n. 
# In the case of a tie, return the smaller odd value. 
# Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0.



def fun_nearestodd(n):
	s = str(n)
	l = s.split('.')
	if (int(l[0]) % 2 == 0):
		if (int(l[1][0]) > 0):
			return int(l[0]) + 1
		else:
			return int(l[0]) - 1
	else:
		return int(l[0])


