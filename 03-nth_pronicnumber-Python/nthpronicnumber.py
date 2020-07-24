# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def isPronicnumber(n):
    k = 1
    flag = 0
    if n == 0:
        return True
    else:
        while (k < n):
            pro = k * (k+1)
            if(pro == n):
                return True
                break
            else:
                k = k+1
        
        else:
            return False

def nthpronicnumber(n):
	c = 0
	i = 0
	while (c <= n):
	    if (isPronicnumber(i)):
	        c = c + 1
	        i = i+1
	    else:
	        i = i+1
	return i - 1
