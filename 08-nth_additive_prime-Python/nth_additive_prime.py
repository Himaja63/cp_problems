# Write the function fun_nth_additive_prime(n) that takes a non-negative int n 
# and returns the nth Additive Prime, which is a prime number such that 
# the sum of its digits is also prime. For example, 113 is prime and 1+1+3==5 and 5 
# is also prime, so 113 is an Additive Prime. fun_nth_additive_prime(0) returns 2


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

def additive(n):
	sum = 0
	while(n!=0):
		rem = n%10
		n = n//10
		sum += rem
	return sum

def fun_nth_additive_prime(n):
	c = 0
	i = 1
	while(c<n+1):
		if (isPrime(i)):
			s = additive(i)
			if (isPrime(s)):
				c = c+1
				i = i+1
			else:
				i = i+1
		else:
			i = i+1
	return i-1
	