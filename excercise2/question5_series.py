# %% Question 5 series
# Avraham Parshan 341419323
from helpers import *

def series(n: int):
    form = lambda i: i / (i+1)
    return list(map(form, range(0, n+1))) #[1,n+1) = [1,n]

def printCurr(j: int):
    print(f"i = {j}, m(i) = {m(j)}")

def m(n):
    # sums up series
    return sum(series(n))

def printSeries(L):
    """
    non functional way
    """
    # loop print i, and the term of sequence fr each i 
    for j in range(1,len(L)):
        print(f"i = {j}, m(i) = {m(j)}")

def printSeriesFunc(n):
    """
    functional way
    range is [x,y), and arrays start from 0 which doesnt interest us
    so i changed to 1, n+1 to meet requirements
    """
    # get same results but without loop - ie with func tools
    return list(map(printCurr,range(1,n+1)))
    
# todo if i have time, find a way to not call m(j) for each term and rather take previous sum and add it to curr
    
def main():
    num = getAndProcessInput()
    if num is None:
        print("Invalid input")
    else:
        # print(f"total sum: {m(num)}")
        # print(f"array: {series(num)}")
        print(f"Actual solution requested:")
        # printSeries(series(num))
        printSeriesFunc(num)
if __name__ == "__main__":
    main()