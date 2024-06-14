# %% Question 1 even print
# Avraham Parshan 341419323
import sys

def evenprt(N1,N2,N3):
    """
    print all even numbers between N1 and N2, and N3 numbers per line
    non - efficient way
    """
    for i in range(N1,N2+1): # [N1,N2]
        if i % 2 == 0: # even numbers in range
            print(i, end=" ")
            if (i-N1) % N3 == 0:  # print N3 numbers per line and 
                print() 

def even_print(val):
    if val == "\n":
        print()
    else:
        print(val, end=" ")
                  
def evenprt_efficient(N1,N2,N3):
    """
    using generators - where we used to print, we now yield and then outside the function we print
    """
    for i in range(N1,N2+1): # [N1,N2]
        if i % 2 == 0: # even numbers in range
            yield i 
            if (i-N1) % N3 == 0:  # print N3 numbers per line and 
                yield "\n"  

def get_check_input():
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
    
    return N1, N2, N3 # return tuple

def main():
    res = get_check_input()
    if not res: # if input is invalid
        sys.exit(1)
        
    N1, N2, N3 = res # unpack tuple
    print("Non-efficient way:")
    evenprt(N1,N2,N3)
    print("\nEfficient way:")
    for i in evenprt_efficient(N1,N2,N3):
        even_print(i)
    
    
    
if __name__ == "__main__":
    main()
