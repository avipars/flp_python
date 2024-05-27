def get_and_process_input(prompt=None, allow_negative=False):
    """
    prompt user for input and ensure its a valid number
    """
    if prompt is None:
        prompt = "Enter number: "
    n = input(prompt)

    try:
        num = int(n)
        if num >= 1: #natural 
            return num
        elif num < 1 and allow_negative: #integer
            return num
        else: #negative
            return None
    except ValueError: #not an int
        return None

def int_to_list(n):
    """from q2 but modified to be arr of string chars
    """
    return list(map(lambda x: str(x), str(n)))


def reverse_num2(n: int):
    """
    use functional version
    trailing zeros in original int are chopped off in new part 
    """
    return ''.join(list(reversed(int_to_list(n))))
