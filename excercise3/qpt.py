from operator import itemgetter
# from functools import reduce
from tailrecurse import *


def shared_keys(d1, d2, d3):
    return d1.keys() & d2.keys() & d3.keys()

def non_shared_keys(d1, d2, d3):
    all_keys = d1.keys() | d2.keys() | d3.keys()
    return all_keys - shared_keys(d1, d2, d3)

def shared_by_2(d1,d2,all_shared):
    return (d1.keys() & d2.keys()) - all_shared

def key_count_in_dicts(key, dicts):
    return sum(1 for d in dicts if key in d)


@tail_call_optimized
def recSum(n, result=0):
    if n == 1:
        return result + 1
    else:
        return recSum(n - 1, result)
    
    
@tail_call_optimized
def add_shared_keys(shared, dicts, result):
    if not shared:
        return result #base case

    key = shared.pop()
    values = []
    for d in dicts:
        if key in d and d[key] not in values:
            values.append(d[key])
    result[key] = tuple(values)

    return add_shared_keys(shared, dicts, result)


@tail_call_optimized
def add_non_shared_keys(non_shared, dicts, result):
    if not non_shared:
        return result

    key = non_shared.pop()
    for d in dicts:
        if key in d:
            if key in result:
                if isinstance(result[key], tuple):
                    if d[key] not in result[key]:
                        result[key] += (d[key],)
                else:
                    result[key] = (result[key], d[key]
                                   ) if result[key] != d[key] else result[key]
            else:
                result[key] = d[key]

    return add_non_shared_keys(non_shared, dicts, result)


def adddicts(d1, d2, d3):
    fully_shared = shared_keys(d1, d2, d3)
    non_shared = list(non_shared_keys(d1, d2, d3))
    dicts = [d1, d2, d3]

  
    fully_shared.sort(key=lambda k: key_count_in_dicts(k, dicts))
    non_shared.sort(key=lambda k: key_count_in_dicts(k, dicts))

    result = add_shared_keys(fully_shared, dicts, {})
    result = add_non_shared_keys(non_shared, dicts, result)
    return result


@tail_call_optimized
def valid_dicts(lst):
    if len(lst) == 0: 
        return True
    elif isinstance(lst[0], dict):
        return valid_dicts(lst[1:])
    else:
        return False


@tail_call_optimized
def getdicts(times:int = 3, results=[]):
    """
    get user input
    """
    if times == 0:
        return results
    else:
        inputVal = eval(input("Enter a dictionary: \n"))
        if not isinstance(inputVal, dict):
            print("Invalid dictionary, try again ")
            return getdicts(times, results)
        else:
            return getdicts(times - 1, results + [inputVal])

def process_stuff(dicts: list):
    """
    print results if dictionaries are valid
    """
    if not valid_dicts(dicts):
      print ("ERROR: dictionary(s) not incorrect!")
    else:
      result_dict = adddicts(*dicts)
      print("Combined\n", result_dict)
      print("Sort by shared\n", sorted(result_dict.items(), key = itemgetter(0)))    

def main():
    # Example usage
    d1 = dict([(1, 'a'), (3, 'd'), (5, 'e')])
    d2 = dict([(1, 'b'), (3, (11, 22)), (7, 'f'), (4, 'q')])
    d3 = dict([(2, 'c'), (3, 'x'), (4, 't'), (8, 'g')])

    user = False
    if user:
        dicts =  getdicts(3)
    else:
        dicts = [d1,d2,d3]
    
    process_stuff(dicts)
if __name__ == "__main__":
    main()
