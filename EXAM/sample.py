from functools import reduce
def myFunction(num):
    return reduce(lambda x, y: x + y, map(lambda z: int(z), list(str(num))))

def myFunction(num):
    def summer(s): #closure
        if not s: # base case
            return 0 # returns 0 if string is empty
        return int(s[0]) + summer(s[1:]) # takes first digit and adds it to the sum of the rest of the digits
            #then calls itself with the rest of the digits
            
    return summer(str(num)) # returns the sum of the digits of the number


def myFunction(n: int):
    """
    regular recursive
    """
    if n < 10:
        return n #base case - 1 digit number
    print(n // 10)
    return myFunction(n // 10) + n % 10 #extract number and add to the sum


if __name__ == "__main__":
    num = 1547
    print(myFunction(num))
    print(myFunctionR(num))