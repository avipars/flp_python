#
# Homework Nr 3 - Q8 - tail recursive
#
from operator import itemgetter

from tailrecurse import tail_call_optimized

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
   print ("item_helper ---\n", "dicts=", dicts, "key=", key, "result=", result)
   if not dicts:
     if len(result) == 1:
       return result[0]
     else:
       return result
   else:
       return item_helper(dicts[1:], key, result + process_item(dicts[0], key))

@tail_call_optimized
def helper1(keys, dicts, result = ()):
   print ("helper1 --- \n", "keys=", keys, "dicts=", dicts, "result=", result)
   print ("-----------")
   if keys == []:
     return result
   else:
     h1 = item_helper(dicts,keys[0])
     print ("h1 = ", h1)
     return helper1(keys[1:],dicts, result + ((keys[0], h1),))
    
def add3dicts(d1,d2,d3):
    allkeys    = d1.keys() | d2.keys() | d3.keys()
    fullshared = d1.keys() & d2.keys() & d3.keys()
    shared12   = (d1.keys() & d2.keys()) - fullshared
    shared13   = (d1.keys() & d3.keys()) - fullshared
    shared23   = (d2.keys() & d3.keys()) - fullshared
    allshared  = fullshared | shared12 | shared13 | shared23
    notshared  = allkeys - allshared
    dicts = (d1,d2,d3)
    h1 = helper1(list(fullshared), dicts)
    print ("h1=", h1)
    h2 = helper1(list(shared12), dicts)
    print ("h2=", h2)
    h3 = helper1(list(shared13), dicts)
    print ("h3=", h3)
    h4 = helper1(list(shared23), dicts)
    print ("h4=", h4)
    h5 = helper1(list(notshared), dicts)
    print ("h5=", h5)
    h = h1 + h2 + h3 + h4 + h5
    print ("h=", h)
    return dict(h)

def q8():
    @tail_call_optimized
    def alldicts(dicts):
        if dicts == []:
          return True
        elif not isinstance(dicts[0], dict):
          return False
        else:
          return alldicts(dicts[1:])
    @tail_call_optimized
    def getdicts(times, Ldicts = []):
       if times == 0:
         return Ldicts
       else:
         inputVal = eval(input("Enter a dictionary: \n"))
         return getdicts(times-1, Ldicts + [inputVal])
    dicts =  getdicts(3)
    if not alldicts(dicts):
      print ("ERROR: Input is incorrect!")
    else:
      result_dict = add3dicts(*dicts)
      print("\nCombined", result_dict)
      print("\nSort by shared", sorted(result_dict.items(), key = itemgetter(0)))    

if __name__ == "__main__":
    q8()

##>>> d1 = dict([(1,'a'),(3,'d'),(5,'e')])
##>>> d2 = dict([(1,'b'), (3,(11,22)), (7,'f'), (4,'q')])
##>>> d3 = dict([(1,'c'), (3,'x'), (4,'t'), (8,'g')])
##>>> add3dicts(d1,d2,d3)
##{1: ('a', 'b', 'c'), 3: ('d', (11, 22), 'x'), 4: ('q', 't'), 8: 'g', 5: 'e', 7: 'f'}
##>>>
