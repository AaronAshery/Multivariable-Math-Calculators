import math
import copy
from graphics import *


def lineOfBestFit(A):  #main function to run,
    #            takes in a "matrix" with each row being a coordinate in 2d
    #            for example A = [[2,1],[0,3],[4,-2]]

    graph(A)
    b = getb(A)
    A = getA(A)
    aT = transpose(A)
    aTA = matrixMultiplication(aT, A)
    aTb = matrixMultiplication(aT, b)
    finalA = []
    for i in range(len(aTb)):
        aTA[i].append(aTb[i][0])
    REF = reducedEchelonForm(aTA)
    b = REF[0][len(REF[0]) - 1]
    m = REF[1][len(REF[1]) - 1]
    return "line of best fit: y = {:.2f} + ({:.2f})x".format(b, m)
        

def getA(A):
    B = []
    C = []
    m = countRows(A)
    for i in range(m):
        B.append(1)
    C.append(B)
    B = []
    for row in A:
        B.append(row[0])
    C.append(B)
    C = transpose(C)
    return C

def getb(A):
    B = []
    C = []
    m = countRows(A)
    for row in A:
        B.append(row[1])
    C.append(B)
    C = transpose(C)
    return C
    


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

    
def matrixMultiplication(A, B):
    m1 = countRows(A)
    n1 = countColumns(A)
    m2 = countRows(B)
    n2 = countColumns(B)
    if n1 != m2:
        return "cannot solve"
    C = []
    D = []
    bTranspose = transpose(B)
    for i in range(m1):
        for j in range(n2):
            val = dotProduct(A[i], bTranspose[j])
            C.append(val)
        D.append(C)
        C = []
    return D
                
    





def countRows(A):
    numRows = 0
    if isinstance(A[0],list) == False:
        numRows = 1
    else:
        for row in A:
            numRows += 1
    return numRows

def countColumns(A):
    if isinstance(A[0], list) == False:
        counter = 0
        for num in A:
            counter += 1
        numColumns = counter
    else:
        numColumns = len(A[0])
    return numColumns

######################
##     GRAPHICS     ##
######################

def graph(A):
    b, m = getFormula(A)
    xMax = A[0][0]
    xMin = A[0][0]
    yMax = A[0][1]
    yMin = A[0][1]
    for row in A:
        if row[0] > xMax:
            xMax = row[0]
        elif row[0] < xMin:
            xMin = row[0]
        else:
            pass
        if row[1] > yMax:
            yMax = row[1]
        elif row[1] < yMin:
            yMin = row[1]
        else:
            pass
    if xMax > yMax:
        maxF = xMax
    else:
        maxF = yMax
    if yMin < xMin:
        minF = yMin
    else:
        minF = xMin
    win = GraphWin("Line of best fit", 400, 400)
    win.setCoords(minF-1,minF-1,maxF+1,maxF+1)
    for row in A:
        c = Circle(Point(row[0],row[1]), .1)
        c.draw(win)
    Line(Point(minF-1, b + (m) * minF-1),Point(maxF+1, b + (m) * maxF+1)).draw(win)
    Line(Point(minF-1,0),Point(maxF+1,0)).draw(win)
    Line(Point(0,minF-1),Point(0,maxF+1)).draw(win)
    

def getFormula(A):
    b = getb(A)
    A = getA(A)
    aT = transpose(A)
    aTA = matrixMultiplication(aT, A)
    aTb = matrixMultiplication(aT, b)
    finalA = []
    for i in range(len(aTb)):
        aTA[i].append(aTb[i][0])
    REF = reducedEchelonForm(aTA)
    b = REF[0][len(REF[0]) - 1]
    m = REF[1][len(REF[1]) - 1]
    return b, m


    
    

######################
##  REF CALCULATOR  ##    
######################

def echelonform(A): 
    copyA = copy.deepcopy(A)
    loopy = True
    counter = 1
    m = countrows(A)
    n = countcolumns(A)   
    A = ech(A)  
    copyA[0] = A[0]
    while loopy == True:
        A = ech(A[1:])
        copyA[counter]=A[0]
        counter += 1
        if len(A) == 1:
            loopy = False
        else:
            pass
    return copyA

def reducedEchelonForm(A): #*MAIN FUNCTION TAKES MATRIX AND TURNS IT INTO REDUCED ECHELON FORM*
    A = echelonform(A)
    copyA = copy.deepcopy(A)
    A = REF(A)
    copyA[-1] = A[-1]
    loopy = True
    counter = countrows(A) - 2
    while loopy == True:
        A = REF(A[:-1])
        copyA[counter]=A[-1]
        counter -= 1
        if len(A) == 1:
            loopy = False
        else:
            pass

    return copyA

def printMatrix(A):
    for i in range(countrows(A)):
        for j in range(countcolumns(A)):
            letter = A[i][j]
            print(round(float(letter),1), end=" ") # keep cursor on same line
        print() # move cursor to next line
    
#takes matrix in echelon form and makes REF for only one layer
def REF(A):
    i = countrows(A) - 1
    j = 0
    loopTest = True
    while loopTest == True:
        if A[i][j] == 0:
            j += 1
            if A[i][j] != 0:
                loopTest = False
            elif j == countcolumns(A) - 1:
                j = 0
                i = i - 1
            else:
                pass
        else:
            loopTest = False
    counter = 0
    for row in A:
        A = kill(A, i, counter, row[j]*-1)
        counter += 1
    return A
            
    


#helper prgram
def ech(A):   
                    #turns column into all 0's except top row makes a pivot of 1
    m = countrows(A)
    n = countcolumns(A)
    counter = 0
    columnCounter = 0
    endLoop = False
    while endLoop == False:
        for row in A: #is first column all 0's?
            if row[columnCounter] == 0:
                counter += 1
                if counter == m:
                    counter = 0
                    columnCounter += 1
                    if columnCounter == countcolumns(A):
                        B = swaps(A, 0, counter)
                        endLoop = True
                        break
                else:
                    pass
            else:
                B = swaps(A, 0, counter)
                endLoop = True
                break
    #B is matrix with pivot in best location, now find what the pivot is
    for row in B:
        for item in row:
            if item != 0:
                ratio = item
                break
            else:
                ratio = 1
                pass
        break
    counter = 0
    columnCounter = 0
    loopCheck = True
    while loopCheck == True: 
        for row in B: #is first column all 0's?
                if columnCounter == countcolumns(B):
                    loopCheck = False
                    #columnCounter = countcolumns(B)
                    break
                else:
                    pass
                if row[columnCounter] == 0:
                    counter += 1
                    if counter == m:
                        counter = 0
                        columnCounter += 1
                    else:
                        pass
                    if columnCounter == countcolumns(B):
                        loopCheck = False
                        columnCounter = countcolumns(B) - 1
                else:
                    loopCheck = False
                    break
    B[0] = scale(B, 0, (1/ratio)) #matrix after first row is scaled by 1/pivot to make pivot a 1
    counter = 0
    for row in B:
        B = kill(B, 0, counter, (row[columnCounter])*-1) #make every number under the pivot a 0 and scale row accordingly
        counter += 1
    return B

def swaps(A, i, j): 
    A[i], A[j] = A[j], A[i]
    return A

def scale(A,i,r):
    D = []
    if countrows(A) == 1:
        for row in A:
            for item in row:
                item = item * r
                D.append(item)
    else:
        for item in A:
            if item == A[i]:
                for num in item:
                    num = num * r
                    D.append(num)
                break
                    
            else:
                pass
    A[i] = D
    return D

def kill(A, i, j, r):  #basically add mult to
    B = []
    C = []
    original = A[i]
    for num in A[i]:
        num = num * r
        B.append(num)
    A[i] = B #B is scaled list
    D = A[i] + A[j] # D is scaled list with list to be changed
    counter = len(D)//2
    for x in range((len(D)//2)):
        new = D[x] + D[counter]
        C.append(new)
        counter += 1
    A[j] = C
    A[i] = original
    return A # A IS NEW MATRIX AFTER ADDED AND STUFF

def countrows(A):
    numRows = 0
    if isinstance(A[0],list) == False:
        numRows = 1
    else:
        for row in A:
            numRows += 1
    return numRows

def countcolumns(A):
    numColumns = len(A[0])
    return numColumns
        



