# % Question 8 combining dictionaries

from operator import itemgetter
from tailrecurse import *


def shared_keys(d1, d2, d3):
    return d1.keys() & d2.keys() & d3.keys()


def non_shared_keys(d1, d2, d3):
    all_keys = d1.keys() | d2.keys() | d3.keys()
    return all_keys - shared_keys(d1, d2, d3)


def key_count_in_dicts(key, dicts):
    """
    non tail recursion to count key in dictionaries
    """
    if not dicts:
        return 0  # base case
    # first is a ternary operator
    return (1 if key in dicts[0] else 0) + key_count_in_dicts(key, dicts[1:])


def add_shared_keys2(shared, dicts, result):
    """
    add shared keys to result
    """
    if not shared:
        return result  # base case

    key = shared.pop()  # remove the last element

    @tail_call_optimized
    def gather_values(dicts, key, values):
        if not dicts:
            return values
        d = dicts[0]
        if key in d and d[key] not in values:
            values.append(d[key])
        return gather_values(dicts[1:], key, values)

    values = gather_values(dicts, key, [])
    result[key] = tuple(values)

    return add_shared_keys2(shared, dicts, result)


def add_non_shared_keys2(non_shared, dicts, result):
    """
    add non shared keys to result
    """
    if not non_shared:
        return result  # base case

    key = non_shared.pop()  # remove the last element

    @tail_call_optimized
    def update_result_with_key(dicts, key, result):
        if not dicts:
            return result
        d = dicts[0]
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
        return update_result_with_key(dicts[1:], key, result)

    result = update_result_with_key(dicts, key, result)

    return add_non_shared_keys2(non_shared, dicts, result)


def adddicts(dicts:list):
    """
    add dictionaries together
    """
    fully_shared = list(shared_keys(*dicts))
    non_shared = list(non_shared_keys(*dicts))
    result = add_shared_keys2(fully_shared, dicts, {})  # add fully shared keys
    result = add_non_shared_keys2(
        non_shared, dicts, result)  # add non shared keys
    return result  # return list of dictionaries


@tail_call_optimized
def valid_dicts(lst):
    """
    check if list of dictionaries is valid
    """
    if len(lst) == 0:
        return True
    elif isinstance(lst[0], dict):
        return valid_dicts(lst[1:])
    else:
        return False


@tail_call_optimized
def get_input(times: int, results=[]):
    """
    get user input, times = # of times to ask/# of dictionaries to get
    results = list of dictionaries
    """
    if times == 0:
        return results
    else:
        inputVal = eval(input("Enter a dictionary: \n"))
        if not isinstance(inputVal, dict):
            print("Invalid dictionary, try again ")
            return get_input(times, results)
        else:
            return get_input(times - 1, results + [inputVal])


def process_stuff(dicts: list):
    """
    print results if dictionaries are valid
    """
    if not valid_dicts(dicts):
        print("ERROR: dictionary(s) not incorrect!")
    else:
        result_dict = adddicts(dicts)
        print("Combined\n", sorted(result_dict.items(),
              key=lambda x: (-len(x[1]) if isinstance(x[1], tuple) else -1, x[0])))
        print("Sort by shared\n", sorted(
            result_dict.items(), key=itemgetter(0)))


def main():
    # Example usage
    d1 = dict([(1, 'a'), (3, 'd'), (5, 'e')])
    d2 = dict([(1, 'b'), (3, (11, 22)), (7, 'f'), (4, 'q')])
    d3 = dict([(2, 'c'), (3, 'x'), (4, 't'), (8, 'g')])

    user = False #user input vs hardcoded 
    if user:
        dicts = get_input(3)
    else:
        dicts = [d1, d2, d3] 

    process_stuff(dicts) # process dictionaries 


if __name__ == "__main__":
    main()
