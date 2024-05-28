from helpers import *
from eratosthenes import napa
# twin primes 1 is a prime btw

def twin_helper(primes):
    return filter(lambda p: p + 2 in primes and p >1, primes)

def twinp(n):
    keys = lambda p: (p, (p + 2, p-2))
    return dict(map(keys, twin_helper(napa(n))))
    
def main():
    num = get_and_process_input()
    if num is None:
        print("Invalid input")
    else:
        print(twinp(num))


if __name__ == "__main__":
    main()
