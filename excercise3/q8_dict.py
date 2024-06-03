# % Question 8 combining dictionaries with recursion
from operator import itemgetter
# from functools import reduce
from tailrecurse import *

def shared_keys(d1, d2, d3):
    return d1.keys() & d2.keys() & d3.keys()

def non_shared_keys(d1, d2, d3):
    all_keys = d1.keys() | d2.keys() | d3.keys()
    return all_keys - shared_keys(d1, d2, d3)

def process_item(D,key):
    #print ("process_item ---\n", "key=", key, "D=", D)
    val = D.get(key)
    if val == None:
        retval = ()
    else:
        retval = (val,)
    #print ("retval=", retval)
    return retval  

#@tail_call_optimized
def item_helper(dicts,key, result = ()):
   #print ("item_helper ---\n", "dicts=", dicts, "key=", key, "result=", result)
   if not dicts:
     if len(result) == 1:
       return result[0]
     else:
       return result
   else:
       return item_helper(dicts[1:], key, result + process_item(dicts[0], key))

@tail_call_optimized
def helper1(keys, dicts, result = ()):
   #print ("helper1 --- \n", "keys=", keys, "dicts=", dicts, "result=", result)
   #print ("-----------")
   if keys == []:
     return result
   else:
     h1 = item_helper(dicts,keys[0])
     #print ("h1 = ", h1)
     return helper1(keys[1:],dicts, result + ((keys[0], h1),))
   
def partial_shared(d1,d2, allshared):
    return (d1.keys() & d2.keys()) - allshared

def adddicts(d1, d2, d3):
    all_keys = d1.keys() | d2.keys() | d3.keys()
    shared_by_all = shared_keys(d1, d2, d3) #shared by all
    non_shared = non_shared_keys(d1, d2, d3)
    shared12 = partial_shared(d1, d2, shared_by_all)
    shared13 = partial_shared(d1, d3, shared_by_all)
    shared23 = partial_shared(d2, d3, shared_by_all)
    
    all_shared = shared_by_all | shared12 | shared13 | shared23
    
    result = {}
    dicts = (d1, d2, d3)
    all_keys = list(shared) + list(non_shared)
    # all_keys.sort(key=lambda k: -key_count_in_dicts(k, dicts))
    # Add keys in sorted order
    for key in all_keys:
        if key in shared:
            values = []
            for d in dicts:
                if key in d and d[key] not in values:
                    values.append(d[key])
            result[key] = tuple(values)
        else:
            for d in dicts:
                if key in d:
                    if key in result:
                        if isinstance(result[key], tuple):
                            if d[key] not in result[key]:
                                result[key] += (d[key],)
                        else:
                            result[key] = (result[key], d[key]) if result[key] != d[key] else result[key]
                    else:
                        result[key] = d[key]

    return result

def main():
    # Example usage
    d1 = dict([(1, 'a'), (3, 'd'), (5, 'e')])
    d2 = dict([(1, 'b'), (3, (11, 22)), (7, 'f'), (4, 'q')])
    d3 = dict([(2, 'c'), (3, 'x'), (4, 't'), (8, 'g')])

    print("Combined dictionary:")
    print(adddicts(d1, d2, d3))

    
if __name__ == "__main__":
    main()
