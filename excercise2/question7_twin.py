from helpers import *
from eratosthenes import napa
#twin primes
# 1 number matters, it and the twin
# 1 to n
# allprimes btwn 1 and n, make a dict has 1 value 
# keys: all prime # btwn 1 and 100
# values = list of twin primes 
# 3,5,

def is_twin(n):
    
    
def twinp(n):
    #dict 
    # return list(filter(form, range(1, n+1)))
    all_prims = napa(n) #list of all primes
    
    list(filter())
def main():
    num = getAndProcessInput()
    if num is None:
        print("Invalid input")
    else:
        print(f"Actual solution requested:")
        print(twinp(num))
        
if __name__ == "__main__":
    main()