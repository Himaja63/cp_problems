# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.


def seperate(num):
	l = []
	for i in range(len(str(num))):
		rem = num % 10
		num = num // 10
		l.append(rem)
	return l

def mostfrequentdigit(n):
	l = seperate(n)
	z = []
	max = 0
	res = l[0]
	for i in l:
		freq = l.count(i)
		if freq >= max:
			max = freq
			res = i
			z.append(res)
	z = list(dict.fromkeys(z))
	low = min(z)
	return low
	