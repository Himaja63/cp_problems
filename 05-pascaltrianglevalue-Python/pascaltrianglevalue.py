# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 


def printPascal(n) :
    s1 = []
    for line in range(0, n) :
        s2 = []
        for i in range(0, line + 1) : 
            # a =  binomialCoeff(line, i)+" "+ end + ""
            a =  binomialCoeff(line, i)
            s2.append(a)
        s1.append(s2)
    return s1
def binomialCoeff(n, k) : 
    res = 1
    if (k > n - k) : 
        k = n - k 
    for i in range(0 , k) : 
        res = res * (n - i) 
        res = res // (i + 1) 
      
    return res 

def fun_pascaltrianglevalue(row, col):
	m = printPascal(row + 1)
	if (col <= (row+1)):
	    return m[row][col]
	else:
	    return 0


