# %% Question 2 natural number sum (done)
# Avraham Parshan 341419323
from helpers import *
from tailrecurse import *


def decompose_digits(n: int) -> list:
    if n == 0:  # Handle the edge case where n is 0
        return [0]
    digits = []
    while n > 0:
        digits.append(n % 10)  # add last digit to array
        n //= 10  # integer division (get rid of last digit)
    return digits  # return array of digits


def sum_digits1(n: int) -> int:
    digits = decompose_digits(n)  # get the digits
    return sum(digits)  # sum the digits


def int_to_list2(n):
    return list(map(lambda x: int(x), str(n)))


def sum_digits2(n):
    return sum(int_to_list2(n))

def reg_recursive(n: int)-> int:
    if n == 0:
        return 0
    return n % 10 + reg_recursive(n // 10)

# tail recursive
def recursive_sum_digits(n: int) -> int:
    @tail_call_optimized
    def helper(n, res):
        if n == 0:
            return res
        return helper(n // 10, res + n % 10)
    return helper(n, 0)

def main():
    n = get_and_process_input(
        prompt="Enter an integer number n (positive or negative): ", allow_negative=True, absolute=True)
    if n == None:
        print("ERROR: Input number is incorrect !")
    else:
        print("With loop: ")
        print(sum_digits1(n))
        print("With functional")
        print(sum_digits2(n))
        print("With regular recursion")
        print(reg_recursive(n))
        print("With tail recursion")
        print(recursive_sum_digits(n))

if __name__ == "__main__":
    main()
