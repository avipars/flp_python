# %% Question 1 Pentagonal Numbers for values >=1
# Avraham Parshan 341419323
import functools
import os
# part a
def pentaNumRange(n1, n2):
    # no loops allowed 
    getPentaNum = lambda n: n*(3*n-1)/2
    return list(map(getPentaNum, range(n1, n2))) #[n1,n2)

# part b
def getAndProcessInput():
    n1 = eval(input("Enter n1: "))
    n2 = eval(input("Enter n2: "))

    # check if n1 < n2, and n1, n2 >= 1 and both are ints
    if(isinstance(n1, int) and isinstance(n2, int) and n1 >= 1 and n2 > 1 and n1 < n2):
        return pentaNumRange(n1,n2)
    else:
        return None

# for loop version
def printWithLoop(pentaList):
    # print 10 items per line
    for i in range(0,len(pentaList),10):
        print(pentaList[i:i+10])
        # if i % 10 == 0: # multiple of 10
        #     print() # new line
        # print(pentaList[i], end=" ") # print item

def printFn(line):
    print(line)
    return None

# # functional programming version
# def printFunctional(pentaList):
#     # list mapped
#     map(printFn, list(map( lambda i : pentaList[i, i+10]), range(0,len(pentaList),10)))
#     return 

def printHelper1(L):
    for i in range(0,len(L),10):
        print(L[i:i+10])
#
def prtprepare(line):
    strLine = map(str,line)
    lstStr  = ','.join(strLine) + '\n'
    return lstStr
#
def printFunctional(L):
    lines = ''.join(map(prtprepare,map(lambda i : L[i:i+10], range(0, len(L), 10))))
    print(lines)
    
def main():
    result = getAndProcessInput()
    if result == None: 
        print("n1 and/or n2 were created invalidly")
    else:
        print("With loop: ")
        printWithLoop(result)
        print("With functional: ")
        printFunctional(result)
        print("Bye")


if __name__ == "__main__":
    main()