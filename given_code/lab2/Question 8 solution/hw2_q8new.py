#
# Homework Nr 2 - Q8
#
from operator import itemgetter
from functools import reduce
  
def dictMerge(D1, D2):
    def crsharedpairs(keyset):
       def helperfunc(key):
         if isinstance(D1[key],tuple):
            return (key, (D1[key],D2[key]))
         else:
            return (key, (D1[key],) + (D2[key],))
       return list(map(helperfunc, keyset))
    def crpairsList(keySet,D):
       return list(map(lambda key : (key, D[key]), keySet)) 
    k1 = set(D1.keys())
    k2 = set(D2.keys())
    sharedKeys = k1 & k2
    onlyD1keys = k1 - k2
    onlyD2keys = k2 - k1
    sharedpairs = crsharedpairs(sharedKeys)
    #print (sharedpairs)
    onlyD1pairs = crpairsList(onlyD1keys,D1)
    #print (onlyD1pairs)
    onlyD2pairs = crpairsList(onlyD2keys,D2)
    #print (onlyD2pairs)
    outDict = dict(sharedpairs + onlyD1pairs + onlyD2pairs)
    #print (outDict)
    return outDict

def add3dicts(d1, d2, d3):
    mergedict = reduce(dictMerge, [d1,d2,d3])
    return mergedict

def q8a():
    dicts = [None, None, None]
    for i in range(3):
      while True:
        inputVal = eval(input("Enter a dictionary: "))
        if isinstance(inputVal,dict):
            dicts[i] = inputVal
            break
        else:
            print ("ERROR: Input value is incorrect!")
    print (add3dicts(dicts[0],dicts[1],dicts[2]))

def q8b():
    dicts = []
    for i in range(3):
      while True:
        inputVal = eval(input("Enter a dictionary: "))
        if isinstance(inputVal,dict):
            dicts += [inputVal]
            break
        else:
            print ("ERROR: Input value is incorrect!")
    print (add3dicts(dicts[0],dicts[1],dicts[2]))

def getdicts(i):
   inputVal = eval(input("Enter a dictionary: "))
   if isinstance(inputVal,dict):
       return inputVal
   else:
       return []
    
def q8c():
    dicts = list(filter(lambda val:isinstance(val,dict), map(getdicts,range(3))))
    if len(dicts) == 3:
      result_dict = add3dicts(dicts[0],dicts[1],dicts[2])
      print("\n", result_dict)
      print("\n", sorted(result_dict.items(), key = itemgetter(0)))
    else:
      print ("ERROR: Input is incorrect!")
    

if __name__ == "__main__":
    q8c()

#
# d1 = dict([(1,'a'),(3,'d'),(5,'e')])
# d2 = dict([(1,'b'), (3,(11,22)), (7,'f'), (4,'q')])
# d3 = dict([(2,'c'), (3,'x'), (4,'t'), (8,'g')])
#
       
#
