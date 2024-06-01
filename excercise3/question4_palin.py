# %% Question 4  palindrome numbers
# Avraham Parshan 341419323
from helpers import *


def is_palindrome(n):
    """
    leading zeros are chopped off (int)
    """
    rev = reverse_num2(n)
    print_result(int(rev) == int(n))

def print_result(res: bool):
    if res:
        print("it is a palindrome!!")
    else:
        print("it is not a palindrome")
        
def is_palindrome_recurse(msg: int):
    # base case
    if msg < 10: #single digit
        return True
    
    first = msg % 10 #get first digit
    last = msg // 10 #get last digit
    if first != last: #compare first and last digits
        return False
    if msg >= 10 and msg <= 99: #2 digit case
        return True 
    
    removed_first = msg % 10
    return is_palindrome_recurse((msg - last * 10) // 10) #strip first and last digits and recurse on the rest


    """
    If the string is made of no letters or just one letter, then it is a palindrome.
    Otherwise, compare the first and last letters of the string.
    If the first and last letters differ, then the string is not a palindrome.
    Otherwise, the first and last letters are the same. Strip them from the string, and determine whether the string that remains is a palindrome. Take the answer for this smaller string and use it as the answer for the original string.
    """


def main():
    num = get_and_process_input(
        prompt="Enter an integer number n (positive or negative): ", allow_negative=True, absolute=True)
    if num is None:
        print("ERROR: Input number is incorrect !")
    else:
        print(is_palindrome(num))
        print("non-tail recurse")
        print(is_palindrome_recurse(num))


if __name__ == "__main__":
    main()
