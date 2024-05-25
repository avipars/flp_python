# %% Question 1 Pentagonal Numbers for values >=1
import functools
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
    for i in range(len(pentaList)):
        if i % 10 == 0: # multiple of 10
            print() # new line
        print(pentaList[i], end=" ") # print item

def printFn(line):
    print(line)
    return None

# functional programming version
def printFunctional(pentaList):
    # list mapped
    listMap = lambda i : pentaList[i, i*10] 
    map(printFn, listMap)

def main():
    result = getAndProcessInput()
    if result == None: 
        print("n1 and/or n2 were created invalidly")
    else:
        printWithLoop(result)

main()