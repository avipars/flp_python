# %% question 4 binary shifting 
# made by avi parshan

def shiftL(binNr,N):
    """
    Shift Left 
    binNr = binary number (in string format)
    N = positive integer which determines how many digits need to be shifted
    """
    return binNr[N:] + N*'0' #string from N on and pad with zeros

def shiftR(binNr,N):
    """
    Shift Right 
    binNr = binary number (in string format)
    N = positive integer which determines how many digits need to be shifted
    """
    return N*"0" + binNr[:-N]


def shiftCL(binNr,N):
    """
    Circular Shift Left 
    binNr = binary number (in string format)
    N = positive integer which determines how many digits need to be shifted
    """
    return binNr[N:] + binNr[:N]

def shiftCR(binNr,N):
    """
    Circular Shift Right 
    binNr = binary number (in string format)
    N = positive integer which determines how many digits need to be shifted
    """
    return binNr[-N:] + binNr[:-N]


def inputFromUser():
    binStr = input("Enter binary number")
    n = int(input("Enter digits to shift by"))
    if n < 0: 
        print("N needs to be positive")
        pass
        
    else:
        print("original:", binStr)
        print("shiftL:", shiftL(binStr,n))
        print("shiftR:", shiftR(binStr,n))
        print("shiftCL:", shiftCL(binStr,n))
        print("shiftCR:", shiftCR(binStr,n))

inputFromUser()

# %%
