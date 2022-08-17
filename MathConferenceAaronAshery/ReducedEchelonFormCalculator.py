#Aaron Ashery
#conference mini project

#reducedEchelonForm is the main function and it takes a 2D list as input
#for example  _     _
        #    | 1 2 3 |
        #    | 4 5 6 | is called by reducedEchelonForm([[1,2,3],[4,5,6],[7,8,9]])
        #    |_7 8 9_|
        #   

import math
import copy

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
    printMatrix(copyA)
    print()
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
        
