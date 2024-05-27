#
# exp.py
#
from tailrecurse import *
#
# Non-recursive, functional version
from functools import reduce
def exp(base,N):
	return reduce(lambda x,y : x*y, map(lambda x : base, range(1,N+1)))
#
# Non-tail recursive version

def exp2(base,N):
   if N == 0:
     return 1
   else:
     return base * exp2(base,N-1)
#
# Tail recursive version

def exp3(base,N):
   @tail_call_optimized
   def Texp(base,N,result):
      if N == 0:
        return result
      else:
        return Texp(base, N-1, base*result)	
   return Texp(base,N,1)
#
