def get_and_process_input(prompt=None, allow_negative=False, absolute=False):
    """
    prompt user for input and ensure its a valid number
    """
    if prompt is None:
        prompt = "Enter number: "
    n = input(prompt)

    try:
        num = int(n)
        if absolute:  # abs value
            return abs(num)
        elif num >= 1:  # natural
            return num
        elif num < 1 and allow_negative:  # integer
            return num
        else:  # negative
            return None
    except ValueError:  # not an int
        return None


def abs(n: int):
    if (n < 0):
        return -n
    else:
        return n


def int_to_list(n):
    """from q2 but modified to be arr of string chars
    """
    return list(map(lambda x: str(x), str(n)))


def reverse_num2(n: int):
    """
    use functional version
    trailing zeros in original int are chopped off in new part 
    """
    return "".join(list(reversed(int_to_list(n))))

def msd(n: int) -> int:
    """
    most significant digit of n, first digit from left
    used for reversing digits and palindrome functions
    """
    return 10**(len(str(n))-1) # highest power of 10 less than or equal to n
    # ie for 1234, it would be 1000 = 10^3
    
def printer(line):
    print(line)
    return None
