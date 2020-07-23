# Background: a Kaprekar number is a non-negative integer, the representation of whose square 
# can be split into two possibly-different-length parts (where the right part is not zero) 
# that add up to the original number again. For instance, 45 is a Kaprekar number, because 
# 45**2 = 2025 and 20+25 = 45. You can read more about Kaprekar numbers here. The first several 
# Kaprekar numbers are: 1, 9, 45, 55, 99, 297, 703, 999 , 2223, 2728,... 
# With this in mind, write the function nthKaprekarNumber(n) that takes a non-negative int n 
# and returns the nth Kaprekar number, where as usual we start counting at n==0.


import math

def isKaprekarnumber(n):
    res = n**2
    s = str(res)
    flag = 0
    if(n == 1):
        return True
    elif(len(s) > 1):
        for i in range(1, len(s)):
            sum = 0
            if(int(s[i:]) != 0 and int(s[:i])+int(s[i:]) == n):
                flag = 1
                break
        if (flag == 1):
            return True
        else:
            return False
    else:
        return False

def fun_nth_kaprekarnumber(n):
    c = 0
    i = 1
    while(c <= n):
        if(isKaprekarnumber(i)):
            c = c+1
            i = i+1
        else:
            i = i+1
    return i - 1