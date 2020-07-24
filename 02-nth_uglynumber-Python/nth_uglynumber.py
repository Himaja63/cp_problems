# Write the function nthUglyNumber that takes a non-negative int n and returns the nth Ugly Number. 
# Ugly numbers are numbers whose only prime factors are 2, 3 or 5. The sequence 1, 2, 3, 4, 5, 6, 8, 
# 9, 10, 12, 15 shows the few ugly numbers. By convention, nthUglyNumber(0) will give 1.

import math
def primeFactors(n):
    res = []
    while n%2 == 0:
        res.append(2)
        n = n/2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n%i == 0:
            res.append(i)
            n = n/i
    if n > 2:
        res.append(n)
    return res

def isUglynumber(n):
    l = primeFactors(n)
    flag = 0
    if n == 1:
        return True
    else:
        for i in l:
            if (i == 2 or i == 3 or i == 5):
                flag = 0
            else:
                flag = 1
        if flag == 0:
            return True
        else:
            return False

def fun_nth_uglynumber(n):
    c = 0
    i = 1
    while(c <= n):
        if (isUglynumber(i)):
            c = c+1
            i = i+1
        else:
            i = i+1
    return i - 1