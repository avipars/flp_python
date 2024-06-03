# %% Question 4  palindrome numbers (done)
# Avraham Parshan 341419323
from helpers import *
from tailrecurse import *


def is_palindrome(n:int):
    """
    leading zeros are chopped off (int)
    """
    rev = reverse_num2(n)
    print_result(int(rev) == int(n))

def print_result(res: bool):
    if res:
        print("it is a palindrome!!")
    else:
        print( "it is not a palindrome")

def is_palindrome_recurse(n: int):
    s = str(n)
    e = len(s)-1
    return recurse_help(s,0,e)

def recurse_help(s:str, start:int, end:int):
    """
    non tail recursive version 
    """
    if s[start] != s[end]:
        return False
    elif start >= end: 
        return True
    else:
        return recurse_help(s, start+1, end -1)
        
def is_palindrome_recursive_r(n):
    """
    regular recursion 
    """
    # Base case: single-digit numbers are always palindromes
    if n < 10:
        return True

    # Get the first and last digits of the number
    first_digit = n // 10**(len(str(n)) - 1)
    last_digit = n % 10

    # Check if the first and last digits match, and recursively check the remaining digits
    return first_digit == last_digit and is_palindrome_recursive_r((n % (10**(len(str(n)) - 1))) // 10)


def is_palindrome_tail_recurse(n):
    """
    tail recursive version 
    """
    @tail_call_optimized
    def helper(s: str, start: int, end: int):
        if start >= end:
            return True
        if s[start] != s[end]: 
            return False
        return helper(s, start + 1, end - 1)  #jump in a level
    s = str(n) #convert to string as its much easier to deal with 
    return helper(s, 0, len(s) - 1) # call tail 
    
def pretty_print(res: bool):
    if res:
        print("It is a palindrome !!")
    else:
        print("It is not a palindrome")
        
def main():
    num = get_and_process_input(
        prompt="Enter an integer number n (positive or negative): ", allow_negative=True, absolute=True)
    if num is None:
        print("ERROR: Input number is incorrect !")
    else:
        print("Functional way")
        is_palindrome(num)
      
        print("Recursive way")
        pretty_print(is_palindrome_recursive_r(num))
        print("Tail Recursive way")
        pretty_print(is_palindrome_tail_recurse(num))

if __name__ == "__main__":
    main()
