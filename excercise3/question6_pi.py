# %% Question 6 pi approximation (done)
# Avraham Parshan 341419323
from helpers import *
from tailrecurse import *

def pi_helper(n): #-1^(i+1) / 2i - 1
    form = (lambda i: ((-1)**(i+1))/(2*i - 1))
    return list(map(form, range(1, n+1))) # n+1 as range is [x,y)

def recursive_pi(n):
    """
    wrapper function for the pi series 
    """
    return 4 * recursive_pi_helper(n) #4 * sum of series


def recursive_pi_helper(n):
    """
    non tail recursive version
    """
    if n == 0: #base case
        return n
    return ((-1)**(n+1))/(2*n - 1) + recursive_pi_helper(n-1) #formula + accumulator

def recursive_pi_t(n):
    """
    tail recursive version of the pi series
    """
    @tail_call_optimized
    def helper(n, res):
        if n == 0:
            return res #base case
        return helper(n - 1, res + ((-1)**(n+1))/(2*n - 1)) #actual tail call 
    return 4 * helper(n, 0) #only happens once 

def print_series(n):
    """
    functional way
    range is [x,y), and arrays start from 0 which doesn't interest us
    so i changed to 1, n+1 to meet requirements
    """
    # get same results but without loop - ie with func tools
    return list(map(print_cur, range(1, n+1)))

def print_cur(j: int): #prints 1 line of the series
    print(f"{j} {m(j)}")


def m(n):
    return sum(4 * pi_helper(n))     # sums up series

def verify(n):
    """
    a non-functional method with for loop to do the same thing and get same result
    """
    sum = 0 
    for i in range(1, n+1): #closed interval
        sum += ((-1)**(i+1)) / (2*i-1)
    return 4*sum

def main():
    num = get_and_process_input()
    if num is None:
        print("Invalid input")
    else:
        print("Loop Version:")
        print(verify(num))
        
        print(f"Functional Version:")
        print_series(num)

        print("Recursive Version:")
        print(recursive_pi(num))
        
        print("Tail Recursive Version:")
        print(recursive_pi_t(num))
if __name__ == "__main__":
    main()
