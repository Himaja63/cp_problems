# Write the function hasnoprimes(L) that takes a 2d list L of integers, 
# and returns True if L does not contain any primes, and False otherwise.

from itertools import chain 

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

def fun_hasnoprimes(l):
	flatten_list = list(chain.from_iterable(l))
	flag = 0
	for i in flatten_list:
		if(isPrime(i)):
			flag = 1
	if(flag == 1):
		return False
	else:
		return True
	
