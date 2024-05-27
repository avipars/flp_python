#
from tailrecurse import *
#
# given a list containing any data items,
# tell if all of them are even numbers
#
def isEvenNum(n):
   return isinstance(n,int) and n >= 0 and n%2 == 0
#
# Non-recursive, functional versions ###
#
def alleven(L):
   return all(map(lambda isEvenNum(x), L))
#
def alleven2(L):
   return len(L) == len((filter(lambda isEvenNum(x), L)))
#
# Non-tail recursive, functional version
def allevenNonTail(L):
   if L == []:
     return True
   else:
     return isEvenNum(L[0]) and allevenNonTail(L[1:])
#
# Tail recursive versions
@tail_call_optimized
def allevenTail1(L):
   if L == []:
     return True
   elif isEvenNum(L[0]):
     return allevenTail1(L[1:])
   else:
     return False
#
@tail_call_optimized
def allevenTail2(L, Acc=True):
   if L == []:
     return Acc
   else:
     return allevenTail2(L[1:], isEvenNum(L[0]) and Acc)
#
# Run examples 
#
##>>> allevenNonTail(list(range(2,20,2)))
##True
##>>> allevenTail1(list(range(2,20,2)))
##True
##>>> allevenTail2(list(range(2,20,2)))
##True
##>>> allevenNonTail(list(range(2,20,3)))
##False
##>>> allevenTail1(list(range(2,20,3)))
##False
##>>> allevenTail2(list(range(2,20,3)))
##False
##>>>
#
    
