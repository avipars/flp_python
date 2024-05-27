# %% Question 6 pi approximator
# Avraham Parshan 341419323
from helpers import *

def pi_helper():
    form = lambda i : ((-1)**(i+1))/(2*i - 1)
    
# def pi(n: int):


def main():
    num = getAndProcessInput()
    if num is None:
        print("Invalid input")
    else:
        # print(f"total sum: {m(num)}")
        # print(f"array: {series(num)}")
        print(f"Actual solution requested:")

if __name__ == "__main__":
    main()