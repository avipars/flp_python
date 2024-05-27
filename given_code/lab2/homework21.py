#
# homework 2.1
#
# A
#
def pentaNumRange(n1,n2):
    getPentaNum = lambda n : n*(3*n - 1) / 2
    return list(map(getPentaNum, range(n1, n2)))
#
# B
#
def printHelper1(L):
    for i in range(0,len(L),10):
        print (L[i:i+10])
#
def prtprepare(line):
    strLine = map(str,line)
    lstStr  = ','.join(strLine) + '\n'
    return lstStr
#
def printHelper2(L):
    lines = ''.join(map(prtprepare,map(lambda i : L[i:i+10], range(0, len(L), 10))))
    print(lines)
#
def prtPentaNums():
    n1 = eval(input("enter the value of n1: "))
    n2 = eval(input("enter the value of n2: "))    
    pentaNums = pentaNumRange(n1, n2)
    printHelper2(pentaNums)
    
