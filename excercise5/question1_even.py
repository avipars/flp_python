# %% Question 1 even print
# Avraham Parshan 341419323
import sys


def evenprt(N1, N2, N3):
    """
    print all even numbers between N1 and N2, and N3 numbers per line
    non - efficient way
    """
    count = 0
    for i in range(N1, N2 + 1):  # [N1,N2]
        if i % 2 == 0:  # even numbers in range
            print(i, end=" ")
            count += 1
            if count % N3 == 0:  # print N3 numbers per line and
                print()  # new line


def evenprt_efficient(N1, N2, N3):
    """
    generator function
    using generators - where we used to print, we now yield and then outside the function we print
    """
    count = 0
    for i in range(N1, N2 + 1):  # [N1,N2]
        if i % 2 == 0:  # even numbers in range
            yield i  # yield instead of print
            count += 1
            if count % N3 == 0:  # print N3 numbers per line and
                yield "\n"   # yield new line


def evenprt_generator(N1, N2, N3):
    """
    we use the generator function to print the values 
    """
    def prt(val): #need this as otherwise it could get a new line and then space in the same run 
        print() if val == "\n" else print(val, end=" ") # ternary operator
        
    for i in evenprt_efficient(N1, N2, N3):  # using generator, gets values from generator
        prt(i) # print values, if we have a new line, then print new line, else print number and a space


def get_check_input():
    """
    get input from user and check if it is valid
    """
    N1 = int(input("Enter a number N1: "))
    N2 = int(input("Enter a number N2: "))
    N3 = int(input("Enter a number N3: "))

    if N1 >= N2:
        print("N1 is greater than or equal to N2, and therefore invalid")
        return False

    # N3 needs to be less than diff
    if N3 >= abs(N2 - N1):
        print("N3 is greater than or equal to the difference between N2 and N1, and therefore invalid")
        return False

    return N1, N2, N3  # return tuple


def main():
    res = get_check_input()
    if not res:  # if input is invalid
        sys.exit(1)

    N1, N2, N3 = res  # unpack tuple
    print("Non-efficient way:")
    evenprt(N1, N2, N3)

    print("\nEfficient way:")
    evenprt_generator(N1, N2, N3)  # using generator


if __name__ == "__main__":
    main()
