# %% Question 4  palindrome numbers
# Avraham Parshan 341419323
from helpers import *
from tailrecurse import *


def is_palindrome(n):
    """
    leading zeros are chopped off (int)
    """
    rev = reverse_num2(n)
    if int(rev) == int(n):
        return "it is a palindrome!!"
    else:
        return "it is not a palindrome"

def is_palindrome_recurse(n):
    def helper(s, start, end):
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return helper(s, start + 1, end - 1)
    
    s = str(n)
    return helper(s, 0, len(s) - 1)

def is_palindrome_tail_recurse(n):
    @tail_call_optimized
    def helper(s, start, end):
        if start >= end:
            return True
        if s[start] != s[end]:
            return False
        return helper(s, start + 1, end - 1)  # Tail recursive call
    s = str(n)
    return helper(s, 0, len(s) - 1)
    
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
        print("Iterative way")
        print(is_palindrome(num))
        print("Recursive way")
        pretty_print(is_palindrome_recurse(num))
        print("Tail Recursive way")
        pretty_print(is_palindrome_tail_recurse(num))

if __name__ == "__main__":
    main()
