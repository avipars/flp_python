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
    fn = (lambda i:  i+2 in all_prims)
    return list(filter(fn, all_prims))


def convert_to_dict(lst):
    fn = (lambda i: i+2)
    return dict(zip(lst, map(fn, lst)))


def twinp(n):
    lst = remove_non_twins(n)
    dct = convert_to_dict(lst)
    return dct


def main():
    num = get_and_process_input()
    if num is None:
        print("Invalid input")
    else:
        print(twinp(num))


if __name__ == "__main__":
    main()
