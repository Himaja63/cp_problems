# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 

def fun_set_kth_digit(n, k, d):
	s = str(n)
	l = [0,0,0,0,0,0,0,0,0,0]
# 	n = int(s[::-1])
	st = ''
	for i in range(len(s)):
		rem = abs(n) % 10
		n = abs(n) // 10
		l[i] = rem
	
	l[k] = d
	for i in l:
		if (i != 0):
			st = st + str(i)
	r = int(st[::-1])
	if (n > 0):
		return r
	else:
		r = r * (-1)
		return r
	