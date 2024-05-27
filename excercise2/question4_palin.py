# %% Question 4  palindrome numbers
# Avraham Parshan 341419323
from helpers import *

def is_palindrome(n):
    """
    leading zeros are chopped off (int)
    """
    rev = reverse_num2(n)
    if int(rev) == int(n):
        return "it is a palindrome!!"
    else:
        return "it is not a palindrome"
    
def main():
    num = get_and_process_input(prompt="Enter an integer number n (positive or negative): ", allow_negative=True,absolute=True)
    if num is None:
        print("ERROR: Input number is incorrect !")
    else:
        print(is_palindrome(num))
        
if __name__ == "__main__":
    main()