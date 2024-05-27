#
# evenlen.py -- computes the number of
#               even numbers in a sequence
#
from tailrecurse import *

def isempty(L):
   return not L  # equivalent to:   return L == []

### How many even numbers are in a list ###

def evenLen1(L):
   if L == []:
     return 0
   elif L[0] % 2 == 0:
     return 1 + evenLen1(L[1:])
   else:
     return evenLen1(L[1:])

def evenLen2(L):
   if L == []:
     return 0
   elif isinstance(L, int) and L[0] % 2 == 0:
     return 1 + evenLen2(L[1:])
   else:
     return evenLen2(L[1:])     

@tail_call_optimized
def evenLen3(L, length=0):
   if L == []:
     return length
   elif isinstance(L, int) and L[0] % 2 == 0:
     return evenLen3(L[1:], length+1)
   else:
     return evenLen3(L[1:], length)
