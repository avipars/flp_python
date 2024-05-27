def getAndProcessInput(prompt = ""):
    if prompt == "":
        n = input("Enter n: ")
    else:
        n = input(prompt)
    # check if n is a valid natural number >=1 (from string)
    if(n.isdigit() and int(n) >= 1):
        return int(n)
    else:
        return None
    
def int_to_list(n):
    """from q2 but modified to be arr of string chars
    """
    return list(map(lambda x: str(x), str(n)))

def reverseNum2(n: int):
    """
    use functional version
    trailing zeros in original int are chopped off in new part 
    """
    return''.join(list(reversed(int_to_list(n))))
