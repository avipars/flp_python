# %% Question 2 natural number sum
# Avraham Parshan 341419323


def getAndProcessInput():
    n = input("Enter n: ")

    # check if n is a valid natural number >=1 (from string)
    if(n.isdigit() and int(n) >= 1):
        return int(n)
    else:
        return None
    
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

def sumDigits2(n):
    l = list(map(lambda x: x*2, 'hello'))

    l = list(map(lambda x: int(x)*2, '123456'))

def main():
    n = getAndProcessInput()
    if n == None: 
        print("n was created invalidly")
    else:
        print(sumDigits1(n))
        # print(sumDigits2(n))
if __name__ == "__main__":
    main()