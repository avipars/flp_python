# %% Question 6 pi approximator
# Avraham Parshan 341419323
from helpers import *

def pi_helper(n):
    form = lambda i : ((-1)**(i+1))/(2*i - 1)
    return list(map(form, range(1, n+1)))

def myprint(line):
    print(line)
    return None

def printSeriesFunc(n):
    """
    functional way
    range is [x,y), and arrays start from 0 which doesnt interest us
    so i changed to 1, n+1 to meet requirements
    """
    # get same results but without loop - ie with func tools
    return list(map(printCurr,range(1,n+1)))

def printCurr(j: int):
    print(f"i = {j}, m(i) = {m(j)}")

def m(n):
    # sums up series
    return sum(series(n))

def main():
    num = getAndProcessInput()
    if num is None:
        print("Invalid input")
    else:
        print(f"Actual solution requested:")

if __name__ == "__main__":
    main()