# Write the function nthCarolPrime(n), which takes a non-negative int and returns the nth Carol Prime, 
# which is a prime number of the form ((2**k - 1)**2 - 2) for some value positive int k. For example, 
# if k equals 3, ((2**3 - 1)**2 -2) equals 47, which is prime, and so 47 is a Carol Prime. 
# The first several Carol primes are: 7, 47, 223, 959, 3967, 16127, 65023, 261119, 1046527,... As such, 
# nthCarolPrime(0) returns 7.
# Note: You must use a reasonably efficient approach that quickly works up to n==9, which 
# will return a 12-digit answer! In particular, this means you cannot just edit isPrime. 
# Hint: you may need to generate only Carol numbers, and then test those as you go 
# for primality (and you may need to think about that hint for a while for it to make sense!).

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

def fun_nth_carolprime(n):
    k = 1
    c = 0
    while(c <= n):
        res = (2**k - 1)**2 - 2
        if(res>0 and isPrime(res)):
            c = c+1
            k = k+1
        else:
            k = k+1
    return res


