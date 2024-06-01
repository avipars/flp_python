from helpers import *
from eratosthenes import napa
from tailrecurse import *

# twin primes 1 is a prime btw


def twin_helper(primes):
    return filter(lambda p: p + 2 in primes and p > 1, primes)


def twinp(n):
    keys = lambda p: (p, (p + 2, p - 2))
    return dict(map(keys, twin_helper(napa(n))))

def twinp_recursive(n):
    def helper(primes, result):
        if len(primes) < 2:
            return result
        else:
            p = primes[0]
            if p + 2 in primes:
                result[p] = (p + 2, p - 2)
            return helper(primes[1:], result)
    return helper(napa(n), {})

# def twinp_tail_recursive(n):
    

def main():
    num = get_and_process_input()
    if num is None:
        print("Invalid input")
    else:
        print("Iterative way")
        print(twinp(num))
        print("Recursive way")
        print(twinp_recursive(num))


if __name__ == "__main__":
    main()
