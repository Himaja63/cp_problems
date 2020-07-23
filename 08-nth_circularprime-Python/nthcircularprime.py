# nthCircularPrime(n) [20 pts]
# Write the function nthCircularPrime that takes a non-negative int n and returns the nth 
# Circular prime, which is a prime number that does not contain any 0's and such that all the 
# numbers resulting from rotating its digits are also prime. The first Circular primes are 2, 3, 
# 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97, 113, 131, 197... To see why 197 is a Circular prime, 
# note that 197 is prime, as is 971 (rotated left), as is 719 (rotated left again).


def isPrime(num):
    flag = 0
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                flag = 1
                break
            else: 
                flag = 0
    else: 
       flag = 1
       
    if (flag == 0):
        return True
    else:
        return False

def rotateLeft(n):
	s = str(n)
	d = 1
	l = []
	res = 0
	while res != n:
		Lfirst = s[0:d]
		Lsecond = s[d:]
		L = Lsecond+Lfirst
		s = L
		res = int(L)
		l.append(res)
	return l

def isCircularprime(n):
	l = rotateLeft(n)
	flag = 0
	for i in l:
		if isPrime(i):
			flag = 0
		else:
			flag = 1
			break
	if flag == 0:
		return True
	else:
		return False

def nthcircularprime(n):
	c = 0
	i = 1
	while(c < n):
		if(i == 11 or i == 111):
			i = i+1
		if(isCircularprime(i)):
			c = c+1
			i = i+1
		else:
			i = i+1
	return i - 1
		