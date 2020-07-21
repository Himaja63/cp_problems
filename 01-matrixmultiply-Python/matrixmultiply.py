# Write the function matrixMultiply(m1, m2) that takes two 2d lists 
# (that we will consider to be matrices) and returns a new 2d list that 
# is the result of multiplying the two matrices. Return None if the 
# two matrices cannot be multiplied for any reason.

def isSquareMatrix(m):
    flag = 0
    for i in range(len(m)):
        for j in range(len(m)):
            if (i != j):
                if(len(m[i]) != len(m[j])):
                    flag = 1
                    break
    if flag == 1:
        return False
    else:
        return True

def isCompatible(m1, m2):
    flag = 0
    if(isSquareMatrix(m1) and isSquareMatrix(m2)):
        if (len(m1[0]) != len(m2)):
            return False
        else:
            return True
    else:
        return False

def fun_matrixmultiply(m1, m2):
    res = []
    for i in range(len(m1)):
        c = []
        for j in range(len(m2[0])):
            c.append(0)
        res.append(c)
    # return res
            
    if(isCompatible(m1, m2)):
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    res[i][j] += m1[i][k]*m2[k][j]
        return res
    else:
        return None



