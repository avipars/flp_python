# %% Question 8 combining dictionaries
# Avraham Parshan 341419323

from helpers import *
from operator import itemgetter
from functools import reduce

# dict combination


def get_items_per_key(k, dicts):
    return (k, tuple(filter(lambda val: val, map(lambda D: D.get(k), dicts))))


def shared_by_dicts(shared_keys, *dicts):
    shared_items = map(lambda k: get_items_per_key(k, dicts), shared_keys)
    return shared_items


def get_not_shared_item(k, *dicts):
    return list(map(lambda D: (k, D[k]), filter(lambda D: k in D, dicts)))


def build_pairs(L, N, rng):
    return list(filter(lambda item: item, map(lambda i: (L[N], L[i]) if N != i else (), rng)))


def auto_cartes(Lst, rng1, rng2):
    cartes = reduce(lambda p1, p2: p1 + p2,
                    map(lambda N: build_pairs(Lst, N, rng2), rng1), [])
    return cartes


def add3dicts(*dicts):
    keys_per_dicts = list(map(lambda D: set(D.keys()), dicts))
    all_keys_in_dicts = reduce(
        lambda all_keys, keys: all_keys | keys, keys_per_dicts[1:], keys_per_dicts[0])

    # looking for keys shared by all the input dictionaries
    keys_shared_by_all_dicts = reduce(
        lambda keys, key: keys & key, keys_per_dicts[1:], keys_per_dicts[0])

    # retrieving pairs (key, (val1, val2, ...)) keys shared by all the dicts
    shared_by_all = list(shared_by_dicts(keys_shared_by_all_dicts, *dicts))

    # looking for keys not shared by all the input dictionaries
    keys_not_shared_by_all_dicts = all_keys_in_dicts - keys_shared_by_all_dicts
    keys_per_dicts_not_shared_by_all = list(
        map(lambda keys: keys - keys_shared_by_all_dicts, keys_per_dicts))

    # looking for keys shared by pairs of dictionaries
    rng1 = range(0, len(keys_per_dicts_not_shared_by_all) - 1)
    rng2 = range(1, len(keys_per_dicts_not_shared_by_all))
    pairs_of_keys_per_dicts_not_shared_by_all = auto_cartes(
        keys_per_dicts_not_shared_by_all, rng1, rng2)
    keys_shared_by_pairs_of_dicts = reduce(lambda keys, key_set: keys | key_set, map(
        lambda keys_pair: keys_pair[0] & keys_pair[1], pairs_of_keys_per_dicts_not_shared_by_all))

    # retrieving pairs (key, (val1, val2, ...)) whose keys are shared by pairs of dicts
    shared_by_pairs_of_dicts = list(shared_by_dicts(
        keys_shared_by_pairs_of_dicts, *dicts))

    # looking for keys not shared at all
    keys_not_shared_at_all = keys_not_shared_by_all_dicts - keys_shared_by_pairs_of_dicts

    # retrieving the pairs (key, val) not shared at all among the dicts
    not_shared_at_all = reduce(
        lambda result, k: result + get_not_shared_item(k, *dicts), keys_not_shared_at_all, [])

    result_list = shared_by_all + shared_by_pairs_of_dicts + not_shared_at_all
    return dict(result_list)


def get_dicts(i):
    inputVal = eval(input("Enter a dictionary: "))
    if isinstance(inputVal, dict):
        return inputVal
    else:
        return []


def main():
    quant = 3 
    dicts = list(filter(lambda val: isinstance(
        val, dict), map(get_dicts, range(quant))))
    if len(dicts) == quant:
        result_dict = add3dicts(*dicts)
        print("\n", result_dict)
        print("\n", sorted(result_dict.items(), key=itemgetter(0)))
    else:
        print("ERROR: Input is incorrect!")


if __name__ == "__main__":
    main()
