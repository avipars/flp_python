# %% Question 4  palindrome numbers
# Avraham Parshan 341419323
from helpers import *


def isPalindrome(n):
    """
    leading zeros are chopped off (int)
    """
    rev = reverseNum2(n)
    if int(rev) == int(n):
        return "it is a palindrome!!"
    else:
        return "it is not a palindrome"
    
def main():
    num = getAndProcessInput()
    if num is None:
        print("Invalid input")
    else:
        print(isPalindrome(num))
        
if __name__ == "__main__":
    main()