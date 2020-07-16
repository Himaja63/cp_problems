# Write the function nthHappyNumber(n) which takes a non-negative integer 
# and returns the nth happy number (where the 0th happy number is 1). 
# Here are some test assertions for you:
# assert(nthHappyNumber(0) == 1)
# assert(nthHappyNumber(1) == 7)
# assert(nthHappyNumber(2) == 10)
# assert(nthHappyNumber(3) == 13)
# assert(nthHappyNumber(4) == 19)
# assert(nthHappyNumber(5) == 23)
# assert(nthHappyNumber(6) == 28)
# assert(nthHappyNumber(7) == 31)


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

def fun_nth_happy_number(n):
	c = 0
	i = 1
	while(c != n+1):
		if(ishappynumber(i)):
			c = c + 1
			i = i + 1
		else:
			i = i + 1
	return i - 1
