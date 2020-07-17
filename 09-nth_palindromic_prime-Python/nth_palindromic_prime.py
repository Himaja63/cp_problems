# Write the function fun_nth_palindromic_prime(n) that takes a non-negative int n 
# and returns the nth palindromic Prime, which is a palidrome number such that 
# it is also a prime. For example, 313 is a palindrome and it is prime 
# so 313 is an palindrome Prime. fun_nth_palindrome_prime(0) returns 2


def palindrome(n):
	sum = 0
	temp = n
	while(n != 0):
		rem = n % 10
		n = n // 10
		sum = sum * 10 + rem
	if (sum == temp):
		return True
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
	
def fun_nth_palindromic_prime(n):
	c = 0
	i = 1
	while (c < n+1):
		if (palindrome(i) and isPrime(i)):
			c = c+1
			i = i+1
		else:
			i = i+1
	return i-1