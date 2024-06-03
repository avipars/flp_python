# %% Question 7 twin primes (done)
# Avraham Parshan 341419323
from helpers import *
from eratosthenes import napa
from tailrecurse import *

# twin primes 1 is a prime btw


def twin_helper(primes):
    return filter(lambda p: p + 2 in primes and p > 1, primes)


def twinp(n):
    keys = lambda p: (p, (p + 2, p - 2))
    return dict(map(keys, twin_helper(napa(n))))

def twinp_recursive(primes: list) -> dict:
    """
    given a list of primes, return a dictionary of twin primes - recursive
    """
    if len(primes) < 2:
        return {} # no twin primes
    else:
        p = primes[0] # first prime
        if p + 2 in primes: # twin prime
            return {p: (p + 2, p - 2), **twinp_recursive(primes[1:])} 
        else:
            return twinp_recursive(primes[1:])
        
def twinp_recursive_t(n):
    """
    # Tail recursive version of twinp
    """
    @tail_call_optimized
    def helper(primes, result):
        if len(primes) < 2:
            return result #base
        else:
            p = primes[0]
            if p + 2 in primes: #check 2 ahead
                result[p] = (p + 2, p - 2) #add to result
            return helper(primes[1:], result) #go in a level
    return helper(napa(n), {}) #start with empty dict


def main():
    num = get_and_process_input()
    if num is None:
        print("Invalid input")
    else:
        print("Iterative way")
        print(twinp(num))

        print("Recursive way")
        print(twinp_recursive(napa(num)))
        print("Tail Recursive way")
        print(twinp_recursive_t(num))


if __name__ == "__main__":
    main()
