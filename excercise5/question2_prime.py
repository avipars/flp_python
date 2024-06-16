# %% Question 2 prime
# Avraham Parshan 341419323
import sys


def napa_prime(N):
    """
    return all prime numbers up to N
    using sieve of Eratosthenes and functional programming tools only ie generators
    """
    p = 2
    for i in range(2, N + 1): # all numbers from 2 to N
        if i == p: # if i is prime
            yield i 
            p = next_prime(p, N) # get the next prime number
        else:
            yield None


def next_prime(p, N):
    """
    return the next prime number after p
    """
    def is_prime(n):
        """
        check if n is a prime number
        """
        for i in range(2, n):
            if n % i == 0:  # if n is divisible by any number other than 1 and itself
                return False
        return True

    for i in range(p + 1, N + 1): # check all numbers from p+1 to N
        if is_prime(i):    # if i is prime
            return i


def sieve(n):
    """
    Returns a generator that yields all prime numbers up to n.
    """
    numbers = (i for i in range(2, n + 1))     # all numbers from 2 to n (inclusive) - generator comprehension
    primes = []  # to store primes found

    while True:
        # get the next number from the generator, if none, return False
        num = next(numbers, False)
        if num is False:  # no more
            break
        yield num  # current number is prime, yield it
        primes.append(num)  # add to list
        numbers = (i for i in numbers if all(i % p != 0 for p in primes)) # generator comprehension - remove multiples of all primes found so far


def print_primes(N, func):
    for i in func(N):  # print each prime (from the yield in the generator)
        print(i, end=" ")  # print the prime separated by a space
    print()  # new line


def prime_factors(N):
    """
    for N > 0, return list with all prime divisors of N 
    """
    factors = [1]  # all numbers are multiples of 1
    for i in sieve(N):
        if N % i == 0:
            factors.append(i)  # add to list
    return factors


def prime_factors_generator(N):
    """
    for N > 0, return list with all prime divisors of N using generators
    """
    yield 1  # always a factor
    for i in sieve(N):  # use the napa gen function
        if N % i == 0:
            yield i  # yield our result


def main():
    print("This program will print all prime numbers up to N")
    N = int(input("Enter a number N: "))
    if N <= 0:
        print("ERROR: the number must be a positive integer")
        sys.exit(1)
    print("All prime numbers up to", N, "are:")

    print_primes(N, sieve)

    print("Prime factors of", N, "are:")
    print(prime_factors(N))

    print("With generator")
    print_primes(N, prime_factors_generator)


if __name__ == "__main__":
    main()
