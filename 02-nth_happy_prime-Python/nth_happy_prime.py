# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).

def numSquareSum(n): 
    squareSum = 0
    while(n): 
        squareSum += (n % 10) * (n % 10)
        n = int(n / 10)
    return squareSum

def ishappynumber(n):
	if (n > 0):
		temp1 = n
		temp2 = n
		while(True):
			temp1 = numSquareSum(temp1)
			temp2 = numSquareSum(numSquareSum(temp2))
			if (temp1 != temp2):
				continue
			else:
				break
		return (temp1 == 1)
	else:
		return False

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


def fun_nth_happy_prime(n):
	c = 0
	i = 1
	while(c != n+1):
		if (ishappynumber(i) and isPrime(i)):
			c = c+ 1
			i = i + 1
		else:
			i = i + 1
	return i - 1

	