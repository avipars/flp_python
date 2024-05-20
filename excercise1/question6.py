# %% convert to dictionary
def print_type(obj):
    print(obj.__class__)

def countDirectElements(lst, dct):
    """
    Count direct elements, str, int, float 
    """
    for i in lst:
        if isinstance(i, (int,float,str,tuple,list)):
            if type(i) not in dct:
                dct[type(i)] = 1
            else:
                dct[type(i)] += 1
        
    return dct


def countAll(lst):
    """
    Count all elements in a list
    """
    # empty dictionary to store counts
    counts = {int: 0, float: 0, str: 0, tuple: 0, list: 0}
    return countDirectElements(lst,counts)

def prettyPrint(dct):
    """
    Pretty print the dictionary, skip if value is 0
    
    """
    print("The list contains:", end=" ")

    total = len(dct)

    cur = 0
    for key in dct:
        count = dct[key]
        if count != 0: #skip if 0
            cur += 1
            print(count, key.__name__ + "s" if count > 1 else key.__name__, end=", " if cur < total else " ") #print the key and value
    print()

    

#main testing function
def main():
    # make
    userInput = eval(input("Enter a list:"))
    prettyPrint(countAll(userInput))
    

#code to work as a module
if __name__ == "__main__":
    main()