# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46

def isTidy(num):
    prev = 10     
    while (num): 
        rem = num % 10
        num //= 10
        if rem > prev: 
            return False
        prev = rem 
    return True 

  

def fun_nth_tidynumber(n):
    c = 0
    i = 1
    while(c != n ):
        if (isTidy(i) == True):
            c = c + 1
        i = i + 1
    return i
   