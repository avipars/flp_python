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
        print("It is a palindrome!!")
    else:
        print( "It is not a palindrome")

def is_palindrome_recurse(n: int):
    """
    used string to make it easier to deal with 
    this is tail recursive
    """

    @tail_call_optimized
    def recurse_help(s:str, start:int = 0, end:int = 1):
        """
        tail recursive helper
        """
        if s[start] != s[end]:
            return False
        elif start >= end: 
            return True
        else:
            return recurse_help(s, start+1, end -1)
    s = str(n) #convert to string as its much easier to deal with 
    e = len(s)-1
    return recurse_help(s,0,e) # call tail with params to start

        
def is_palindrome_recursive_r(n):
    """
    regular recursion 
    """
    # Base case: single-digit numbers are always palindromes
    if n < 10:
        return True

    # Get the first and last digits of the number
    first_digit = n // msd(n) #call a helper fn i made
    last_digit = n % 10

    # Check if the first and last digits match, and recursively check the remaining digits
    return first_digit == last_digit and is_palindrome_recursive_r((n % (msd(n))) // 10)


def pretty_print(res: bool):
    print("It is a palindrome !!") if res else print("It is not a palindrome")
        
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
        pretty_print(is_palindrome_recurse(num))

if __name__ == "__main__":
    main()
