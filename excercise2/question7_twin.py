from helpers import *
from eratosthenes import napa
# twin primes
# 1 number matters, it and the twin
# 1 to n
# allprimes btwn 1 and n, make a dict has 1 value
# keys: all prime # btwn 1 and 100
# values = list of twin primes
# 3,5,


def remove_non_twins(n):
    all_prims = napa(n)  # list of all primes
    def fn(x): return x+2 in all_prims
    return list(filter(fn, all_prims))


def convert_to_dict(lst):
    def fn(x): return x+2
    return dict(zip(lst, map(fn, lst)))

def twinp(n):
    lst = remove_non_twins(n)
    dct = convert_to_dict(lst)
    return format_twin(dct)

def printer(key, val):
    print(f"key: {key}, val")
def format_twin(dct):
    # functional way to print stuff in dic

def main():
    num = getAndProcessInput()
    if num is None:
        print("Invalid input")
    else:
        print(f"Actual solution requested:")
        print(twinp(num))


if __name__ == "__main__":
    main()