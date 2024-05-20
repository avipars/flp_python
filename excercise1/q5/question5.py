# %% question 5 list of lists
# Edited by avi parshan

def getNestedTuples(lst):
    """
    part a
    Creates a list whose elements are the 
    elements of all the tuples nested inside the input list
    returns in list
    """
    tupleList = [] # blank list for tuples
    for i in lst: #go through OG list
        if isinstance(i, tuple): #if element is a tuple
            for j in i: #go through tuple
                tupleList.append(j) #add each item to new list
    return tupleList #return new list

def getNestedLists(lst):
    """
    part b
    Creates a tuple whose elements are the elements of all the 
    lists nested inside the input list
    returns in tuple
    """
    listList = [] # blank list for lists
    for i in lst: #go through OG list
        if isinstance(i, list): #if element is a list
            for j in i: #go through list
                listList.append(j) #add each item to new list 

    #did it this way cause a tuple is immutable meaning it will make a new object each time we append to it... so 
    return tuple(listList)  #return new tuple of list (immutable)

def getNumbersFromListWithoutDuplicates(lst):
    """
    part c
    Creates a tuple whose elements are the numbers contained in the input list, 
    which are not contained in any of the nested lists or tuple
    """
    numNested = [] # blank list for numbers
    for i in lst: #go through OG list
        # check nested lists, tuples
        if isinstance(i, list) or isinstance(i, tuple):
            for j in i: #go through nested lists
                if isinstance(j, (int, float)): #if element is a number
                    numNested.append(j) #add to new list
    goodList = [] 
    for i in lst: #go through OG list
        if isinstance(i, (int, float)) and i not in numNested:
            goodList.append(i)
        # # now check the outer list and add numbers that are also not in nested
        # if isinstance(i, (int, float)) and i not in numNested:
        #     numNested.append(i)
    return tuple(goodList) #return new tuple of numbers (immutable)

def getStringsNotInNest(lst):
    """
    part d
    Creates a list whose elements are the strings contained in the input list, 
    which are not contained in any of the nested lists or tuples.
    """
    strNested = []
    for i in lst:
        # check nested lists, tuples
        if isinstance(i, list) or isinstance(i, tuple):
            for j in i: #go through nested lists
                if isinstance(j, str): #if element is a string
                    strNested.append(j) #add to new list

    goodList = []
    # now we check outer strings and add to new list if not in nested
    for i in lst:
        if isinstance(i, str) and i not in strNested:
            goodList.append(i)

    return goodList #return new list of strings

#main function to test the functions
def main():
    userInput = eval(input("Enter a list:"))
    print(getNestedTuples(userInput))
    print(getNestedLists(userInput))
    print(getStringsNotInNest(userInput))
    print(getNumbersFromListWithoutDuplicates(userInput))

#code to work as a module
if __name__ == "__main__":
    main()
# %%
