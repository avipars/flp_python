from helpers import *
from operator import itemgetter
from functools import reduce

#dict combination

def add3dicts(d1, d2, d3):
    return reduce(dictMerge, [d1,d2,d3])

def main():
    dicts = list(filter(lambda val:isinstance(val,dict), map(getdicts,range(3))))
    if len(dicts) == 3:
      result_dict = add3dicts(dicts[0],dicts[1],dicts[2])
      print("\n", result_dict)
      print("\n", sorted(result_dict.items(), key = itemgetter(0)))
    else:
      print ("ERROR: Input is incorrect!")
    


if __name__ == "__main__":
    main()