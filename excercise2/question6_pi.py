# %% Question 6 pi approximator
# Avraham Parshan 341419323
from helpers import *

def pi_helper(n):
    form = (lambda i: ((-1)**(i+1))/(2*i - 1))
    return list(map(form, range(1, n+1)))


def print_series(n):
    """
    functional way
    range is [x,y), and arrays start from 0 which doesn't interest us
    so i changed to 1, n+1 to meet requirements
    """
    # get same results but without loop - ie with func tools
    return list(map(print_cur, range(1, n+1)))

def print_cur(j: int):
    print(f"{j} {m(j)}")


def m(n):
    # sums up series
    return sum(4 * pi_helper(n))


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




if __name__ == "__main__":
    main()
