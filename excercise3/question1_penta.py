# %% Question 1 Pentagonal Numbers for values >=1 - ex3 (done)
# Avraham Parshan 341419323
from tailrecurse import *

# part a


def penta_num_range(n1, n2):
    # no loops allowed
    penta = (lambda n: n * (3 * n - 1) / 2)
    return list(map(penta, range(n1, n2)))  # [n1,n2)

# part b

def penta_non_tail_recursive(n1: int, n2: int) -> list:
    """
    Provide start and end, get list of pentagonal numbers back.
    """
    if n1 == n2:
        return []
    else:
        current_value = n1 * (3 * n1 - 1) / 2
        rest_of_values = penta_non_tail_recursive(n1 + 1, n2)
        return [current_value] + rest_of_values
    
@tail_call_optimized
def penta_recursive(n1: int, n2: int, result: list = []) -> list:
    """
    provide empty list and get results back in the list  - tail recursive version
    """
    if n1 == n2:
        return result
    else:
        result.append(n1 * (3 * n1 - 1) / 2)
        return penta_recursive(n1 + 1, n2, result)

# used for the functional-loop variants
def get_process_input(n1: int, n2: int):

    # check if n1 < n2, and n1, n2 >= 1 and both are ints
    if (isinstance(n1, int) and isinstance(n2, int) and n1 >= 1 and n2 > 1 and n1 < n2):
        return penta_num_range(n1, n2)
    else:
        return None



def get_and_process_input():
    n1 = eval(input("Enter n1: "))
    n2 = eval(input("Enter n2: "))

    # check if n1 < n2, and n1, n2 >= 1 and both are ints
    if (isinstance(n1, int) and isinstance(n2, int) and n1 >= 1 and n2 > 1 and n1 < n2):
        # return penta_num_range(n1, n2)
        return (n1, n2)
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

def print_functional(L):
    """
    every 10 numbers get a new line
    """
    print(''.join(
        map(prnt, map(lambda i: L[i:i + 10], range(0, len(L), 10)))))


def print_with_recursive(pentaList: list, index:int=0):
    """
    Recursive version printing, with every 10 numbers getting a new line
    """
    if index >= len(pentaList): #index out of bounds - base
        return

    if index > 0 and index % 10 == 0: #divisible by 10
        print() #new line for 10 breaks

    print(pentaList[index], end=" ") #print curr

    print_with_recursive(pentaList, index + 1) # go to next


def main():
    result = get_and_process_input()
    if result == None:
        print("ERROR: the values must be positive integers and n2 > n1")
    else:
        n1 = result[0]
        n2 = result[1]
        res_old = get_process_input(n1, n2)
        print("1st loop:")
        print_with_loop_old(res_old)
        print("\n2nd loop: ")
        print_with_loop(res_old)
        print("With functional: ")
        print_functional(res_old)
        print("\nWith recursion: ")
        print_with_recursive(penta_non_tail_recursive(n1,n2))
        print("With tail recursion:")
        print_with_recursive(penta_recursive(n1, n2))


if __name__ == "__main__":
    main()
