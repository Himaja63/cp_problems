# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.
import math
def primeFactors(n):
    res = []
    while n%2 == 0:
        res.append(2)
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            res.append(i)
            n = n/i
    if n > 2:
        res.append(n)
    return res

def isPowerfulnumber(n):
	l = primeFactors(n)
	flag = 0
	if n == 1:
	    return True
	else:
		for i in l:
			p = i**2
			if(n % p == 0):
			    flag = 0
			else:
			    flag = 1
			    break
		if(flag == 0):
		    return True
		else:
		    return False

def nthpowerfulnumber(n):
	c = 0
	i = 1
	while (c <= n):
		if(isPowerfulnumber(i)):
			c = c+1
			i = i+1
		else:
			i = i+1
	return i-1
	

	
	