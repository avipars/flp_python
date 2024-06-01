# %% Question 1 Pentagonal Numbers for values >=1 - ex3
# Avraham Parshan 341419323
import functools
import os

from tailrecurse import *

# part a


def penta_num_range(n1, n2):
    # no loops allowed
    penta = (lambda n: n * (3 * n - 1) / 2)
    return list(map(penta, range(n1, n2)))  # [n1,n2)

# part b

def penta_recursive(n1, n2, result):
    if n1 == n2:
        return result
    else:
        result.append(n1 * (3 * n1 - 1) / 2)
        return penta_recursive(n1 + 1, n2, result)
    



def get_and_process_input():
    n1 = eval(input("Enter n1: "))
    n2 = eval(input("Enter n2: "))

    # check if n1 < n2, and n1, n2 >= 1 and both are ints
    if (isinstance(n1, int) and isinstance(n2, int) and n1 >= 1 and n2 > 1 and n1 < n2):
        return penta_num_range(n1, n2)
    else:
        return None


def print_with_loop(lst):
    """
    Better looking and less code
    """
    skip_by = 10    # print 10 items per line
    for i in range(0, len(lst), skip_by):
        # was this before         print(pentaList[i:i+10])
        print(*lst[i:i + skip_by])
        # but that gave us something looking like an array


def print_with_loop_old(pentaList):
    """
    easier to understand but more code
    """
    for i in range(0, len(pentaList)):
        if (i % 10 == 0) and i > 0:  # multiple of 10 dont print first blank
            print()  # new line
        print(pentaList[i], end=" ")  # print item


def print_helper1(L):
    for i in range(0, len(L), 10):
        print(L[i:i + 10])


def prnt(line):
    strLine = map(str, line)
    lstStr = ' '.join(strLine) + '\n'
    return lstStr
#


def print_functional(L):
    """
    every 10 numbers get a new line
    """
    print(''.join(
        map(prnt, map(lambda i: L[i:i + 10], range(0, len(L), 10)))))


def main():
    result = get_and_process_input()
    if result == None:
        print("ERROR: the values must be positive integers and n2 > n1")
    else:
        # print("1st loop:")
        # print_with_loop_old(result)
        # print("2nd loop: ")
        # print_with_loop(result)
        # print("With functional: ")
        # print_functional(result)
 
        
        print("With non-tail recursion: ")
        print("With tail recursion")
        print("Bye")
if __name__ == "__main__":
    main()
