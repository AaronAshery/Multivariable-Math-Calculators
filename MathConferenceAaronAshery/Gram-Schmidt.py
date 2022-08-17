import math

def gramSchmidt2(span):
    m = countVectors(span)
    orthog = []
    orthog.append(span[0])
    counter = 0
    for i in range(m-1):
        counter += 1
        total = []
        for j in range(counter):
            u = orthog[j]
            v = span[counter]
            proj = projection(v,u)
            total.append(proj)
        for i in range(len(total)):
            v = vectorSubtraction(v,total[i])
        orthog.append(v)
    printSpan(orthog)
    print()
    return orthog

def projection(v, u):
    dot = dotProduct(u, v)
    distance = distanceOfSquared(u)
    w = vectorMultiplyScalar((dot / distance), u)
    return w


def dotProduct(u, v):
    m = len(u)
    n = len(v)
    if m == n:
        total = 0
        for i in range(m):
            mult = (u[i] * v[i])
            total = total + mult
        return total
    else:
        return "vectors are of unequal length"

def distanceOfSquared(v):
    total = dotProduct(v,v)
    return total

def vectorMultiplyScalar(c, v):
    m = len(v)
    w = []
    for num in v:
        num = num*c
        w.append(num)
    return w

def vectorSubtraction(u,v):
    m = len(u)
    n = len(v)
    w = []
    if m == n:
        for i in range(m):
            w.append(u[i] - v[i])
        return w
    else:
        return "vectors are of unequal length"

def countVectors(A):
    numVectors = 0
    if isinstance(A[0],list) == False:
        numVectors = 1
    else:
        for row in A:
            numVectors += 1
    return numVectors

def printSpan(A):
    for i in range(len(A[0])):
        for j in range(countVectors(A)):
            letter = A[j][i]
            print(round(float(letter),1), end="  ") # keep cursor on same line
        print() # move cursor to next line



