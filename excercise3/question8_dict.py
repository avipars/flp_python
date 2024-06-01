# % Question 8 combining dictionaries
from operator import itemgetter
from functools import reduce
from tailrecurse import *

# dict combination


def get_items_per_key(key, dicts):
    """
    Returns a tuple (key, (val1, val2, ...)) for the given key shared across dictionaries.
    """
    return (key, tuple(filter(lambda val: val, map(lambda d: d.get(key), dicts))))


def shared_by_dicts(shared_keys, *dicts):
    """
    Finds items shared by the specified keys across dictionaries.
    """
    return map(lambda key: get_items_per_key(key, dicts), shared_keys)


def get_not_shared_item(key, *dicts):
    """
    find items not in common
    """
    return list(map(lambda d: (key, d[key]), filter(lambda d: key in d, dicts)))


def build_pairs(L, N, range):
    """
    given a list L, a number N, and a range, return a list of pairs (L[N], L[i]) for i in range
    """
    return list(filter(lambda item: item, map(lambda i: (L[N], L[i]) if N != i else (), range)))


def auto_cartes(lst, range1, range2):
    """
    cartesian product of pairs of lists
    """
    return reduce(lambda p1, p2: p1 + p2,
                  map(lambda N: build_pairs(lst, N, range2), range1), [])


def combine_dictionaries(*dicts):
    keys_per_dicts = list(map(lambda d: set(d.keys()), dicts))
    all_keys_in_dicts = reduce(
        lambda all_keys, keys: all_keys | keys, keys_per_dicts[1:], keys_per_dicts[0])  # OR - take all (union)

    # looking for keys shared by all the input dictionaries
    keys_shared_by_all_dicts = reduce(
        lambda keys, key: keys & key, keys_per_dicts[1:], keys_per_dicts[0])  # AND - take common (intersection)

    # retrieving pairs (key, (val1, val2, ...)) keys shared by all the dicts
    shared_by_all = list(shared_by_dicts(keys_shared_by_all_dicts, *dicts))

    # look for keys not shared by all the input dictionaries
    keys_not_shared_by_all_dicts = all_keys_in_dicts - keys_shared_by_all_dicts
    keys_per_dicts_not_shared_by_all = list(
        map(lambda keys: keys - keys_shared_by_all_dicts, keys_per_dicts))  # set difference

    # look for keys shared by pairs of dictionaries
    range1 = range(len(keys_per_dicts_not_shared_by_all) - 1)
    range2 = range(1, len(keys_per_dicts_not_shared_by_all))

    pairs_of_keys_per_dicts_not_shared_by_all = auto_cartes(
        keys_per_dicts_not_shared_by_all, range1, range2)

    keys_shared_by_pairs_of_dicts = reduce(lambda keys, key_set: keys | key_set, map(
        lambda keys_pair: keys_pair[0] & keys_pair[1], pairs_of_keys_per_dicts_not_shared_by_all))

    # retrieving pairs (key, (val1, val2, ...)) whose keys are shared by pairs of dicts
    shared_by_pairs_of_dicts = list(shared_by_dicts(
        keys_shared_by_pairs_of_dicts, *dicts))

    # look for keys not shared at all
    keys_not_shared_at_all = keys_not_shared_by_all_dicts - keys_shared_by_pairs_of_dicts

    # retrieving the pairs (key, val) not shared at all among the dicts
    not_shared_at_all = reduce(
        lambda result, key: result + get_not_shared_item(key, *dicts), keys_not_shared_at_all, [])

    result_list = shared_by_all + shared_by_pairs_of_dicts + \
        not_shared_at_all  # principle of inclusion-exclusion
    return dict(result_list)


def get_dicts(i):
    """
    get user input for dictionary, i is not used
    """
    input_val = eval(input("Enter a dictionary: "))
    return input_val if isinstance(input_val, dict) else []


def main():
    quant = 3  # combining 3 dictionaries
    dicts = list(filter(lambda val: isinstance(
        val, dict), map(get_dicts, range(quant))))

    if len(dicts) == quant:
        result_dict = combine_dictionaries(*dicts)
        print("\nCombined dictionary:")
        print("\n", result_dict)
        print("\nSorted by shared:")
        print("\n", sorted(result_dict.items(), key=itemgetter(0)))
    else:
        print("ERROR: Input is incorrect!")


if __name__ == "__main__":
    main()
