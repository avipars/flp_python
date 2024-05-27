# %% Question 3 reverse ints
# Avraham Parshan 341419323
from helpers import *


def reverseNum0(n: int):
    """
    basic way to reverse
    """
    cop = n #dont  change input
    reverse = 0 #sum 
    while(cop > 0):
        reverse = reverse * 10 + cop % 10
        cop //=  10 #integer division
    return reverse

def reverseNum1(n: int): 
    """
    use splice/slice to reverse string
    """
    arr = str(n)[::-1] #convert to string, then use python trick
    return int(arr)

def main():
    num = getAndProcessInput()
    if num is None:
        print("Invalid input")
    else:
        print("basic way loop")
        print(reverseNum0(num))
        print("list reverse slice")
        print(reverseNum1(num))
        print("functional way")
        print(reverseNum2(num))

if __name__ == "__main__":
    main()
# %%
