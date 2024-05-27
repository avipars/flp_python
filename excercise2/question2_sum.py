# %% Question 2 natural number sum
# Avraham Parshan 341419323
from helpers import *
    
def decompose_digits(n: int) -> list:
    if n == 0:  # Handle the edge case where n is 0
        return [0] 
    digits = [] 
    while n > 0:
        digits.append(n % 10) #add last digit to array 
        n //= 10 # integer division (get rid of last digit)
    return digits # return array of digits

def sumDigits1(n: int) -> int:
    digits = decompose_digits(n) # get the digits
    return sum(digits) # sum the digits

def int_to_list2(n):
    return list(map(lambda x: int(x), str(n)))

def sumDigits2(n):
    return sum(int_to_list2(n))

def main():
    n = getAndProcessInput()
    if n == None: 
        print("n was created invalidly")
    else:
        print("With loop: ")
        print(sumDigits1(n))
        print("with functional")
        print(sumDigits2(n))
if __name__ == "__main__":
    main()