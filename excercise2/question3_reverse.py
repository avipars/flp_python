# %% Question 3 reverse ints
# Avraham Parshan 341419323

def getAndProcessInput():
    n = input("Enter n: ")

    # check if n is a valid natural number >=1 (from string)
    if(n.isdigit() and int(n) >= 1):
        return int(n)
    else:
        return None

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



def int_to_list(n):
    """from q2 but modified to be arr of string chars
    """
    return list(map(lambda x: str(x), str(n)))

def reverseNum2(n: int):
    """
    use functional version
    """
    return''.join(list(reversed(int_to_list(n))))

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
