# Write the function nthSmithNumber that takes a non-negative int n 
# and returns the nth Smith number, where a Smith number is a composite (non-prime) 
# the sum of whose digits are the sum of the digits of its prime factors (excluding 1). 
# Note that if a prime number divides the Smith number multiple times, its digit sum 
# is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is 
# counted twice, thus making 4 a Smith Number.
# so fun_nthsmithnumber(0) should return 4
# so fun_nthsmithnumber(1) should return 22

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

def sumOfDigits(n):
    add = 0
    while(n!=0):
        rem = n% 10
        n = n // 10
        add = add+rem
    return add

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

def smithNumber(n):
    add = 0
    l = primeFactors(n)
    if (isPrime(n)):
        return False
    else:
        for i in range(len(l)):
            add += sumOfDigits(l[i])
        if add == sumOfDigits(n):
            return True
        else:
            return False

def fun_nth_smithnumber(n):
    c = 0
    i = 2
    while(c <= n):
        if(smithNumber(i)):
            c = c+1
            i = i+1
        else:
            i = i+1
    return i-1
