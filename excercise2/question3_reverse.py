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
    num = get_and_process_input("Enter an integer number n (positive or negative): ", allow_negative=True)
    if num is None:
        print("ERROR: Input number is incorrect !")
    else:
        sign = -1 if num < 0 else 1 #ternary

        print("basic way loop")
        print(sign*reverse_num0(abs(num)))
        print("list reverse slice")
        print(sign*reverse_num1(abs(num)))
        print("functional way")
        # functional way - in helper file as used > 1 time
        print(sign*reverse_num2(abs(num)))

if __name__ == "__main__":
    main()
# %%
