# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math

def isKaprekarnumber(n):
    res = n**2
    s = str(res)
    flag = 0
    if (n == 1):
        return True
    elif(len(s) > 1):
        for i in range(1,len(s)):
            sum = 0
            if (int(s[i:]) != 0 and int(s[:i])+int(s[i:]) == n):
                flag = 1
                break
        if (flag == 1):
            return True
        else:
            return False
    else:
        return False


def fun_nearestkaprekarnumber(n):
    i = n-1
    j = n+1
    res = 0
    while(True):
        if(isKaprekarnumber(i)):
            res = i
            break
        if(isKaprekarnumber(j)):
            res = j
            break
        else:
            i = i - 1
            j = j + 1
    return res
    