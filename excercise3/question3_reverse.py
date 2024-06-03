# %% Question 3 reverse ints (done)
# Avraham Parshan 341419323
from helpers import *
from tailrecurse import *


def reverse_num0(n: int):
    """
    basic way to reverse
    """
    cop = n  # dont  change input, use this as temp version 
    reverse = 0  # sum
    while (cop > 0):
        reverse = reverse * 10 + cop % 10
        cop //= 10  # integer division
    return reverse


def reverse_num1(n: int):
    """
    use splice/slice to reverse string
    """
    arr = str(n)[::-1]  # convert to string, then use python trick
    return int(arr)

def reverse_recurse(n: int):
    """
    recursive way to reverse (non tail)
    """
    if n == 0 or n == 1:
        return n #base
    else:
        mo = n % 10 # first
        fl = n // 10 #lst
        
        return mo * 10**(len(str(n))-1) + reverse_recurse(fl)

#using tail recursion and closure
def reverse_recursive_t(n: int):
    """
    Closure and tail recursion
    """
    @tail_call_optimized
    def helper(n:int, res:int):  #n is number, result is the accumulator
        if n == 0:
            return res
        return helper(n // 10, res * 10 + n % 10) # go in a level
    return helper(n, 0)
    
def main():
    num = get_and_process_input(
        "Enter an integer number n (positive or negative): ", allow_negative=True)
    if num is None:
        print("ERROR: Input number is incorrect !")
    else:
        sign = -1 if num < 0 else 1  # ternary operator, i said if they give a negative number, reverse it and put back the negative sign
        inp = abs(num)
        
        print("basic way loop")
        print(sign*reverse_num0(inp))
        print("list reverse slice way")
        print(sign*reverse_num1(inp))
        print("functional way")
        # functional way - in helper file as used > 1 time
        print(sign*int(reverse_num2(inp)))
        print("Recursive way")
        print(sign*reverse_recurse(inp))
        print("Tail recursive way")
        print(sign*reverse_recursive_t(inp))

if __name__ == "__main__":
    main()
# %%
