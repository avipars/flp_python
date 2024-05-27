#
# mylen.py -- computes the size of a sequence
#
from tailrecurse import *

def isempty(L):
   return not L  # equivalent to:   return L == []
#
# Non-recursive, functional version
def mylen1(L):
   return sum(map(lambda x : 1, L))
#
# Non-tail recursive version
def mylen2(L):
   if isempty(L):
     return 0
   else:
     return 1 + mylen2(L[1:])
#
# Tail recursive version
@tail_call_optimized
def myLen3(L):
   def Tlen(L,length):
      if L == []:  # if not L:
        return length
      else:
        return Tlen(L[1:], 1 + length)	
   return Tlen(L,0)

@tail_call_optimized
def mylen4(L, length=0):
    if L == []:  # if not L:
      return length
    else:
      return mylen4(L[1:], length+1)

@tail_call_optimized
def mylen5(L, length=0):
    if isempty(L):
      return length
    else:
      return mylen5(L[1:], length+1)
