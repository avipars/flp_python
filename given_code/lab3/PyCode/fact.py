#
# fact.py
#
from tailrecurse import *
#
# Non-recursive, functional version
from functools import reduce
def fact1(N):
	return reduce(lambda x,y : x*y, range(1,N+1))
#
# Non-tail recursive version

def fact2(N):
   if N in (0,1):
     return 1
   else:
     return N * fact2(N-1)
#
# Tail recursive version

def fact3(N):
   @tail_call_optimized
   def Tfact(N,result):
      if N in (0,1):
        return result
      else:
        return Tfact(N-1, N*result)	
   return Tfact(N,1)
#
