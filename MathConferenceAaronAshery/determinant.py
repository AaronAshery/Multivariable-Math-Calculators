import math
import copy

def determinantMxN(A):   #Main function that takes a square matrix and gets the det(A)
    if countRows(A) <= 3:
        return determinant3x3(A)
    elif countRows(A) == 4:
        return determinant4x4(A)
    else:
        counter = 1
        B = []
        total = 0
        k = 0
        At = transpose(A)
        for i in range(countRows(A)):
            co = A[0][i]
            k = 0
            for j in range(countRows(A)-1):
                if k == i:
                    k += 1
                B.append(At[k][1:])
                k += 1
            total = total + (co * counter * determinantMxN(B))
            B = []
            counter = counter * -1
        return total
        
        

def determinant4x4(A):
    if (countRows(A) != countColumns(A)) or (countRows(A) != 4):
        return "Must be a 4x4 matrix"
    else:
        counter = 1
        B = []
        total = 0
        k = 0
        At = transpose(A)
        for i in range(countRows(A)):
            co = A[0][i]
            k = 0
            for j in range(countRows(A)-1):
                if k == i:
                    k += 1
                B.append(At[k][1:])
                k += 1
            total = total + (co * counter * determinant3x3(B))
            B = []
            counter = counter * -1
    return total





def determinant3x3(A):
    if countRows(A) != countColumns(A):
        return "Must be a square matrix"
    if countRows(A) == 2:
        ad = A[0][0] * A[1][1]
        bc = A[0][1] * A[1][0]
        return (ad - bc)
    elif countRows(A) == 1:
        return A[0][0]
    else:
        diag1 = 1
        diag2 = 1
        total = 0
        m = 0
        n = 0
        for j in range(countRows(A)):
            for i in range(countRows(A)):
                diag1 = diag1 * A[m][n]
                m, n = getNextForwards(A,m,n)
            for i in range(countRows(A)):
                diag2 = diag2 * A[m][n]
                m, n = getNextBackwards(A,m,n)
            total = total + (diag1 - diag2)
            n += 1
            diag1 = 1
            diag2 = 1
        return total



def getNextForwards(A,m,n):
    position = A[m][n]
    m += 1
    n += 1
    if n > countColumns(A) - 1:
        n = 0
    if m > countRows(A) - 1:
        m = 0
    return m, n

def getNextBackwards(A,m,n):
    position = A[m][n]
    m +=1
    n -=1
    if n < 0:
        n = countColumns(A) - 1
    if m > countRows(A) - 1:
        m = 0
    return m, n
            



def countRows(A):
    numRows = 0
    if isinstance(A[0],list) == False:
        numRows = 1
    else:
        for row in A:
            numRows += 1
    return numRows

def countColumns(A):
    numColumns = len(A[0])
    return numColumns

def transpose(A):
    n = countColumns(A)
    m = countRows(A)
    B = []
    C = []
    for i in range(n):
        for row in A:
            B.append(row[i])
        C.append(B)
        B = []
    return C

