#
# getpairs.py
#
# Non-recursive, functional version
from functools import reduce
def getpairs1(L):
   return filter(lambda isinstance(item,(list,tuple)) and len(item) == 2, L)
#
# Non-tail recursive version
def getpairs2(L):
   if L == []:
     return []
   elif isinstance(L[0],(list,tuple)) and len(L[0]) == 2:
     return getpairs2(L[1:]) + [L[0]]
   else:
     return getpairs2(L[1:])
#
# Tail recursive version
def getpairs3(L):
   def Tgetpairs(L,Lout):
      if L == []:
        return Lout
      elif isinstance(L[0], (list,tuple)) and len(L[0]) == 2:
        return Tgetpairs(L[1:], Lout+[L[0]])
      else:
        return Tgetpairs(L[1:], Lout)                 
   return Tgetpairs(L,[])
#
