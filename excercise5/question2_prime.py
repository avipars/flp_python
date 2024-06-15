# %% Question 2 prime
# Avraham Parshan 341419323
import sys

def napa_prime(N):
    """
    return all prime numbers up to N
    using sieve of Eratosthenes and functional programming tools only ie generators
    """
    p = 2
    for i in range(2, N + 1):
        if i == p:
            yield i
            p = next_prime(p, N)
        else:
            yield None

def next_prime(p, N):
    """
    return the next prime number after p
    """
    for i in range(p + 1, N + 1):
        if is_prime(i):
            return i
    

def is_prime(n):
    """
    check if n is a prime number
    """
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
def sieve(n):
    """
    Returns a generator that yields all prime numbers up to n.
    """
    
    numbers = (i for i in range(2, n + 1)) # all numbers from 2 to n (inclusive) - generator comprehension
    primes = [] #to store primes found

    while True:
        num = next(numbers, False) # get the next number from the generator, if none, return False

        if num is False: #no more
            break

        yield num #current number is prime, yield it

        primes.append(num) # add to list
        
        numbers = (i for i in numbers if all(i % p != 0 for p in primes)) #generator comprehension - remove multiples of all primes found so far

def print_primes(N):
    for i in sieve(N): # print each prime (from the yield in the generator)
        print(i, end=" ") # print the prime separated by a space
    print() # new line

def prime_factors(N):
    """
    for N > 0, return list with all prime divisors of N 
    """
    factors = [1]
    for i in sieve(N):
        if N % i == 0:
            factors.append(i)
    return factors


def prime_factors_generator(N):
    """
    for N > 0, return list with all prime divisors of N using generators
    """
    
    pass
def main():
    print("This program will print all prime numbers up to N")
    N = int(input("Enter a number N: "))
    if N <= 0:
        print("ERROR: the number must be a positive integer")
        sys.exit(1)
    print("All prime numbers up to", N, "are:")
    
    print_primes(N)

    print("Prime factors of", N, "are:")
    print(prime_factors(N))

    
if __name__ == "__main__":
    main()

