# %%
# Part a 
# made by avi parshan

import random 
def areNumbers(nums):
    """
    Checks if all the arguments are numbers (integer or float).
    
    Args:
    nums: list of numbers
    
    Returns:
    bool: True if all arguments are numbers, False otherwise.
    """
    for num in nums:
        try:
            float(num) #convert to float to check if it is a number
        except ValueError:
            return False
    return True

def convertAllToNumbers(nums):
    """
    Convert all the elements in a list to numbers.
    
    Args:
    nums (list): A list of elements.
    
    Returns:
    list: A list containing the elements converted to numbers.
    """
    for i in range(len(nums)):
        if "." in nums[i]: 
            nums[i] = float(nums[i])
        else:
            nums[i] = int(nums[i])
    return nums

def getAllInputs():
    """
    Get input from the user and check if they are numbers.
    
    Returns:
    list: A list containing the numbers entered by the user.
    """
    try:
        num1 = input("Enter the first number: ")
        num2 = input("Enter the second number: ")
        num3 = input("Enter the third number: ")
        num4 = input("Enter the fourth number: ")
        l = [num1, num2, num3, num4] #list of numbers
        if areNumbers(l):
            return convertAllToNumbers(l) #converts to list
        else:
            return None #invalid input
    except ValueError:
        return None #invalid input 

def middleNumbersA(nums):
    """
    Find the middle two numbers from a list of numbers. (version1 using sorted)
    
    Args:
    nums (list): A list of numbers.
    
    Returns:
    list: A list containing the middle two numbers.
    """
    arr = sorted(nums) #sort the numbers
    return [arr[1], arr[2]] #return the middle two numbers

# Part A Q3 with our own sort-select 

def random_partition(arr, l, r):
    """
    uses the quick select algorithm we learned in DSA2
     """
    pivot_index = random.randint(l, r) #random pivot
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index] #swap pivot with last element 
    pivot = arr[r] #pivot is last element
    i = l - 1 #index of smaller element

    for j in range(l, r): #iterate through array
        if arr[j] <= pivot: #if element is less than pivot
            i += 1 #increment index
            arr[i], arr[j] = arr[j], arr[i] #swap elements

    arr[i + 1], arr[r] = arr[r], arr[i + 1] #swap pivot with element at i + 1
    return i + 1 #return index of pivot

def kth_smallest(arr, l, r, k):
    """
    kth or ith order statistic using quick select algorithm
    """
    if k > 0 and k <= r - l + 1: #if k is valid
        pos = random_partition(arr, l, r) #get partition index
        if pos - l == k - 1: #if position is kth element
            return arr[pos] #return element
        elif pos - l > k - 1: #if position is greater than kth element
            return kth_smallest(arr, l, pos - 1, k) #recurse on left side
        else:
            return kth_smallest(arr, pos + 1, r, k - pos + l - 1) #recurse on right side
         
def middleNumbersB(nums):
    """
    Find the middle two numbers from a list of numbers. (version2 no built in sort)
    
    Args:
    nums (list): A list of numbers.
    
    Returns:
    list: A list containing the middle two numbers.
    """
    # arr = list(nums) #copy over 
    arr = nums
    n = len(arr)
    if n % 2 == 0:
        # This // operator divides the first number by the second number and rounds the result down to the nearest integer (FLOOR division)
        return [kth_smallest(arr, 0, n - 1, n // 2), kth_smallest(arr, 0, n - 1, n // 2 + 1)]
    else:
        return [kth_smallest(arr, 0, n - 1, n // 2 + 1), kth_smallest(arr, 0, n - 1, n // 2 + 1)]
    
def main():
    """
    Main function to run the program.
    """
    nums = getAllInputs()
    if nums is not None:
        print("The middle numbers are (method 1 - using sort()):", middleNumbersA(nums)) 
        print("The middle numbers are (method 2):", middleNumbersB(nums))
    else:
        print("Invalid input! Please enter numbers only.")

main()


# %%
# Part b - generalized version of program in part a, uses tuples

def areNumbers(nums):
    """
    Checks if all the arguments are numbers (integer or float).
    
    Args:
    nums: tuple of numbers (as strings)
    
    Returns:
    bool: True if all arguments are numbers, False otherwise.
    """
    for i in nums:
        try:
            float(i) #convert to float to check if it is a number
        except ValueError:
            return False
    return True


def getAllInputs():
    """
    get tuple of any length, if is tuple and all elements are numbers
    """
    try:
        nums = eval(input("a tuple of numbers")) #get input eval to convert to tuple (or try)
        if areNumbers(nums): #check if all strings inside are numbers
            return nums 
        else:
            return None
    except ValueError:
        return None
    
def middleNumbersA(nums):
    """
    Find the middle two numbers from a tuple of numbers. (version1 using sorted)
    
    Args:
    nums (tuple): A tuple of numbers.
    
    Returns:
    tuple: A tuple containing the middle two numbers.
    """
    arr = sorted(list(nums)) #sort the numbers
    n = len(arr)     # list size is not preset
    if n % 2 == 0: #if even number of elements
        return (arr[n // 2 - 1], arr[n // 2])
    else: #if odd number of elements
        return (arr[n // 2], arr[n // 2])


def random_partition(arr, l, r):
    """
    uses the quick select algorithm we learned in DSA2
     """
    pivot_index = random.randint(l, r) #random pivot
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index] #swap pivot with last element 
    pivot = arr[r] #pivot is last element
    i = l - 1 #index of smaller element

    for j in range(l, r): #iterate through array
        if arr[j] <= pivot: #if element is less than pivot
            i += 1 #increment index
            arr[i], arr[j] = arr[j], arr[i] #swap elements

    arr[i + 1], arr[r] = arr[r], arr[i + 1] #swap pivot with element at i + 1
    return i + 1 #return index of pivot

def kth_smallest(arr, l, r, k):
    """
    kth or ith order statistic using quick select algorithm
    """
    if k > 0 and k <= r - l + 1: #if k is valid
        pos = random_partition(arr, l, r) #get partition index
        if pos - l == k - 1: #if position is kth element
            return arr[pos] #return element
        elif pos - l > k - 1: #if position is greater than kth element
            return kth_smallest(arr, l, pos - 1, k) #recurse on left side
        else:
            return kth_smallest(arr, pos + 1, r, k - pos + l - 1) #recurse on right side
        
def middleNumbersB(nums):
    """
    Find the middle two numbers from a tuple of numbers. (version2 no built in sort)
    
    Args:
    nums (tuple): A tuple of numbers.
    
    Returns:
    tuple: A tuple containing the middle two numbers.
    """
    arr = list(nums) #copy over 
    n = len(arr)
    if n % 2 == 0:
        # This // operator divides the first number by the second number and rounds the result down to the nearest integer (FLOOR division)
        return (kth_smallest(arr, 0, n - 1, n // 2), kth_smallest(arr, 0, n - 1, n // 2 + 1)) #return middle two elements
    else:
        return (kth_smallest(arr, 0, n - 1, n // 2 + 1), kth_smallest(arr, 0, n - 1, n // 2 + 1)) #return middle two elements 
    
    
def main():
    """
    Main function to run the program.
    """
    nums = getAllInputs()
    if nums is not None: #if valid input
        # choses the 2 middle numbers from the unsorted tuple
        print("The middle numbers are (method 1 - using sort()):", middleNumbersA(nums)) 
        print("The middle numbers are (method 2):", middleNumbersB(nums))
    else:
        print("Invalid input! Please enter a valid tuple of numbers.")

main()


# %% part C - get a tuple and throw out non numbers and then do the same as part b
import random
def getAllInputs():
    """
    get tuple of any length, if is tuple and all elements are numbers
    """
    try:
        nums = eval(input("a tuple of numbers")) #get input eval to convert to tuple (or try)
        return cleanedTuple(nums)
    except ValueError:
        return None
    
def cleanedTuple(nums):
    """
    remove non numbers from tuple and return tuple
    """
    cleaned = [] #new list
    for i in nums:
        try:
            # if it is another data type, ignore it
            if(isinstance(i, float) or isinstance(i, int)):
                cleaned.append(i) #if successful, add to new list
            else: 
                pass #whatever it is, ignore it
        except ValueError: #if not a number
            pass
    return tuple(cleaned) #return tuple

def middleNumbersA(nums):
    """
    Find the middle two numbers from a tuple of numbers. (version1 using sorted)
    
    Args:
    nums (tuple): A tuple of numbers.
    
    Returns:
    tuple: A tuple containing the middle two numbers.
    """
    arr = sorted(list(nums)) #sort the numbers
    n = len(arr)     # list size is not preset
    if n % 2 == 0: #if even number of elements
        return (arr[n // 2 - 1], arr[n // 2])
    else: #if odd number of elements
        return (arr[n // 2], arr[n // 2])
    
def middleNumbersB(nums):
    """
    Find the middle two numbers from a tuple of numbers. (version2 no built in sort)
    
    Args:
    nums (tuple): A tuple of numbers.
    
    Returns:
    tuple: A tuple containing the middle two numbers.
    """
    arr = list(nums) #copy over 
    n = len(arr)
    if n % 2 == 0:
        # This // operator divides the first number by the second number and rounds the result down to the nearest integer (FLOOR division)
        return (kth_smallest(arr, 0, n - 1, n // 2), kth_smallest(arr, 0, n - 1, n // 2 + 1)) #return middle two elements
    else:
        return (kth_smallest(arr, 0, n - 1, n // 2 + 1), kth_smallest(arr, 0, n - 1, n // 2 + 1)) #return middle two elements


def random_partition(arr, l, r):
    """
    uses the quick select algorithm we learned in DSA2
     """
    pivot_index = random.randint(l, r) #random pivot
    arr[pivot_index], arr[r] = arr[r], arr[pivot_index] #swap pivot with last element 
    pivot = arr[r] #pivot is last element
    i = l - 1 #index of smaller element

    for j in range(l, r): #iterate through array
        if arr[j] <= pivot: #if element is less than pivot
            i += 1 #increment index
            arr[i], arr[j] = arr[j], arr[i] #swap elements

    arr[i + 1], arr[r] = arr[r], arr[i + 1] #swap pivot with element at i + 1
    return i + 1 #return index of pivot


def kth_smallest(arr, l, r, k):
    """
    kth or ith order statistic using quick select algorithm
    """
    if k > 0 and k <= r - l + 1: #if k is valid
        pos = random_partition(arr, l, r) #get partition index
        if pos - l == k - 1: #if position is kth element
            return arr[pos] #return element
        elif pos - l > k - 1: #if position is greater than kth element
            return kth_smallest(arr, l, pos - 1, k) #recurse on left side
        else:
            return kth_smallest(arr, pos + 1, r, k - pos + l - 1) #recurse on right side

def main():
    """
    Main function to run the program.
    """
    nums = getAllInputs()
    if nums is not None: #if valid input
        # choses the 2 middle numbers from the unsorted tuple
        print("The middle numbers are (method 1 - using sort()):", middleNumbersA(nums)) 
        print("The middle numbers are (method 2):", middleNumbersB(nums))
    else:
        print("Invalid input! Please enter a valid tuple of numbers.")


main()
# %%
