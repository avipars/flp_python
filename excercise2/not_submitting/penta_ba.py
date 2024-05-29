# %% Question 1 Pentagonal Numbers for values >=1
# Avraham Parshan 341419323
import sys
from helpers import *
#

# # functional programming version
# def print_functional(pentaList):
#     # list mapped
#     map(print_fn, list(map( lambda i : pentaList[i, i+10]), range(0,len(pentaList),10)))
#     return

def pentaNumRange(n1, n2):
    return list(map(lambda n: n*(3*n-1)/2, range(n1, n2)))


def get_and_process_input():
    n1 = eval(input("Enter n1: "))
    n2 = eval(input("Enter n2: "))

    # check if n1 < n2, and n1, n2 >= 1 and both are ints
    if (isinstance(n1, int) and isinstance(n2, int) and n1 >= 1 and n2 > 1 and n1 < n2):
        return (n1, n2)
    else:
        return None



def get2nums():
    n1 = eval(input("enter the value of n1: "))
    n2 = eval(input("enter the value of n2: "))
    if isinstance(n1, int) and n1 > 0 and isinstance(n2, int) and n1 < n2:
        return n1, n2
    return False

def print_with_loop(lst):
    """
    Better looking and less code
    """
    skip_by = 10    # print 10 items per line
    for i in range(0, len(lst), skip_by):
        # was this before         print(pentaList[i:i+10])
        print(*lst[i:i+skip_by])
        # but that gave us something looking like an array


def print_with_loop_old(pentaList):
    """
    easier to understand but more code
    """
    for i in range(0, len(pentaList)):
        if (i % 10 == 0) and i > 0:  # multiple of 10 dont print first blank
            print()  # new line
        print(pentaList[i], end=" ")  # print item



def pentaprt(L):
    return map(printer, list(map(lambda i: L[i:i+10], range(0, len(L), 10))))


def main():
    inValues = get_and_process_input()
    if inValues is None:
        print("ERROR: the input is incorrect!")
        sys.exit()
        
    n1, n2 = inValues
    
    result = pentaNumRange(n1, n2)
    print("old loop:")
    print_with_loop_old(result)
    print("new loop: ")
    print_with_loop(result)
    print("With functional: ")
    list(pentaprt(result))
    print("Bye")

if __name__ == "__main__":
    main()