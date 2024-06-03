# %% Question 5 series (done)
# Avraham Parshan 341419323
from helpers import *
from tailrecurse import *


def series(n: int):
    form = (lambda i: i / (i + 1))
    return list(map(form, range(0, n + 1)))  # [1,n+1) = [1,n]


def m(n):
    # sums up series
    return sum(series(n))


def print_one(j: int):
    print(f"{j} {m(j)}")


def print_series_loop(L: list):
    """
    non functional way
    """
    # loop print i, and the term of sequence fr each i
    for j in range(1, len(L)):
        print_one(j)


def print_series(n: int):
    """
    functional way
    range is [x,y), and arrays start from 0 which doesn't interest us
    so i changed to 1, n+1 to meet requirements
    """
    # get same results but without loop - ie with func tools
    return list(map(print_one, range(1, n + 1)))

def recurse_series(n):
    """
    non tail recursive version
    """
    # base case n = 1
    assert n >= 1, "n must be >= 1"
    if n == 1:
        res = 0.5
    else:     # i / (i + 1)
        res = n / (n + 1) + recurse_series(n - 1)
    print(f"{n}: {res}")
    return res
        
#tail
@tail_call_optimized
def recurse_series_t(n, acc=0.5):
    """
    tail recursive version
    """
    # Base case: n = 1
    print(f"{n}: {acc}")
    if n == 1:
        return acc
    else:
        return recurse_series_t(n - 1, acc + n / (n + 1))
    
def main():
    num = get_and_process_input("Enter a Natural number n: ")
    if num is None:
        print("ERROR: Input number is incorrect!")
    else:
        print("Loop Version:")
        print_series_loop(series(num))
        print("Functional version:")
        print_series(num)
        
        print("Recursive version:")
        recurse_series(num)
        
        print("Tail Recursive version:")
        print(recurse_series_t(num))

if __name__ == "__main__":
    main()
