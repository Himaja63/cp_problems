# Write the function sumOfSquaresOfDigits(n) which takes a non-negative integer and returns the 
# sum of the squares of its digits. Here are some test assertions for you:
# assert(sumOfSquaresOfDigits(5) == 25)   # 5**2 = 25
# assert(sumOfSquaresOfDigits(12) == 5)   # 1**2 + 2**2 = 1+4 = 5
# assert(sumOfSquaresOfDigits(234) == 29) # 2**2 + 3**2 + 4**2 = 4 + 9 + 16 = 29

def sumofsquaresofdigit(n):
	sum = 0
	while(n!=0):
		rem = n%10
		n = n//10
		sum = sum + rem**2
	return sum
