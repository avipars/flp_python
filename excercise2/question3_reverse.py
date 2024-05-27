# %% Question 3 reverse ints
# Avraham Parshan 341419323
from helpers import *


def reverse_num0(n: int):
    """
    basic way to reverse
    """
    cop = n #dont  change input
    reverse = 0 #sum 
    while(cop > 0):
        reverse = reverse * 10 + cop % 10
        cop //=  10 #integer division
    return reverse

def reverse_num1(n: int): 
    """
    use splice/slice to reverse string
    """
    arr = str(n)[::-1] #convert to string, then use python trick
    return int(arr)

def main():
    num = get_and_process_input("Enter an integer number n (positive or negative): ", True)
    if num is None:
        print("Invalid input")
    else:
        print("basic way loop")
        print(reverse_num0(num))
        print("list reverse slice")
        print(reverse_num1(num))
        print("functional way")
        print(reverse_num2(num))

if __name__ == "__main__":
    main()
# %%
