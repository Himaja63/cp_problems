# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….

MAX_ITERATIONS = 25

def isPalindrome(n):
	sum = 0
	temp = n
	while(n != 0):
		rem = n%10
		n = n // 10
		sum = sum*10 + rem
	if(sum == temp):
		return True
	else:
		return False

def isLychrel(number):    
    for i in range(MAX_ITERATIONS):
        # print(number)
        number = number + int(str(number)[::-1])
          
        if (isPalindrome(number)):  
            return False 
      
    return True

def nthlychrelnumbers(n):
	# your code goes here
	c = 0
	i = 196
	while(c < n):
		if(isLychrel(i)):
			c = c+1
			i = i+1
		else:
			i = i+1
	return i - 1
			 