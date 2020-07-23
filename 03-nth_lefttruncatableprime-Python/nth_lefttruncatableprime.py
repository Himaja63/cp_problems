# Write the function nthLeftTruncatablePrime(n).
# A Left-truncatable prime is a prime which in a given base (say 10) does not contain 0 
# and which remains prime when the leading (left) digit is successively removed. 
# For example, 317 is left-truncatable prime since 317, 17 and 7 are all prime. 
# There are total 4260 left-truncatable primes.
# So nthLeftTruncatablePrime(0) retunearestKaprekarNumber(n)rns 2, and 
# nthLeftTruncatablePrime(10) returns 53.



import math

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

def isLeftTruncatablePrime(n):
    flag = 0
    s = str(n)
    i = 0
    if '0' in s:
        return False
    else:
        while(i < len(s)):
            if(isPrime(int(s[i:]))):
                flag = 0
                i = i+1
            else:
                flag = 1
                break
        if(flag == 0):
            return True
        else:
            return False
    

def fun_nth_lefttruncatableprime(n):
    c = 0
    j = 1
    while(c <= n):
        if(isLeftTruncatablePrime(j)):
            c = c+1
            j = j+1
        else:
            j = j+1
    return j-1

    