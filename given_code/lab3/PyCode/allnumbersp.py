# allnumbersp.py
#
from tailrecurse import *
from functools import reduce
#
# given a list containing any data items,
# tell if all of them, at the top level, are numbers 
#
def isnumber(X):
   return isinstance(X,(int,float))
#
# Non-recursive, functional versions
def allnumbersA(L): # using the filter high order function
  return len(L) == len(filter(isnumber, L))

def allnumbersB(L):
  # using a composition of map and reduce high order functions
  return reduce(lambda x,y : x and y,map(isnumber,L))  

def allnumbersC(L): # using a composition of the "all" function and 
                    # the map high order function
  return all(map(isnumber, L))
#
# tail recursive versions of allnumbersp(L)
@tail_call_optimized
def allnumbersp1(L): # without an accumulator parameter
   if L == []:
     return True
   elif isnumber(L[0]):
     return allnumbersp1(L[1:])  # this is a tail call
   else:
     return False

@tail_call_optimized
def allnumbersp2(L, result = True): # with an accumulator parameter, called here 'result'
   if L == []:
     return result
   else:
     return allnumbersp2(L[1:], result and isinstance(L[0], (int, float)))
#
# non-tail recursive version of allnumbersp(L)
def allnumbersp3(L):
   if len(L) == 1:
     return isinstance(L[0], (int, float))
   else:
     return isinstance(L[0], (int, float)) and allnumbersp3(L[1:])
#
##
def keepNonumbers(L):
   if not L:
     return []
   elif allnumbersp2(L[0]):
     return keepNonumbers(L[1:])
   else:
     return [L[0]] + keepNonumbers(L[1:])
#
#
##>>> allnumbersp1([1,5,3,'a'])
##False
##>>> allnumbersp2([1,5,3,'a'])
##False
##>>> allnumbersp3([1,5,3,'a'])
##False
##>>> allnumbersp1([1,5,3,10])
##True
##>>> allnumbersp2([1,5,3,10])
##True
##>>> allnumbersp3([1,5,3,10])
##True
##>>> 
