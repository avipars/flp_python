#
# zugiCountWpatterns.py
#
from functools import reduce
from tailrecurse import *
#
def zugi(N):
   return N%2 == 0
#
def isNum(x):
   return isinstance(x,(int, float))
#
# zugiCountF implemented using List Comprehension
def zugiCountF1(L):
   return len([N  for N in [item for item in L  if isNum(item)]  if zugi(N)])
def zugiCountF2(L):
   return len([item for item in L  if isNum(item) and zugi(item)])
#
# zugiCountF implemented using non-tail recursion
def zugiCountF3a(L):
   def zugiCountRec(L):
     if L == []:
       return []
     elif isNum(L[0]) and zugi(L[0]):
       return [L[0]] + zugiCountRec(L[1:])
     else:
       return zugiCountRec(L[1:])
   return len(zugiCountRec(L))
#
def zugiCountF3b(L):
   def zugiCountRec(L):
     if L == []:
       return 0
     elif isNum(L[0]) and zugi(L[0]):
       return 1 + zugiCountRec(L[1:])
     else:
       return zugiCountRec(L[1:])
   return zugiCountRec(L)
#
# zugiCountF implemented using tail recursion
def zugiCountF4a(L):
   @tail_call_optimized
   def zugiCountTail(L,result=[]):
     if L == []:
       return result
     elif isNum(L[0]) and zugi(L[0]):
       return zugiCountTail(L[1:], [L[0]] + result)
     else:
       return zugiCountTail(L[1:], result)
   return len(zugiCountTail(L))
#
def zugiCountF4b(L):
   @tail_call_optimized
   def zugiCountTail(L,result=0):
     if L == []:
       return result
     elif isNum(L[0]) and zugi(L[0]):
       return zugiCountTail(L[1:], 1 + result)
     else:
       return zugiCountTail(L[1:], result)
   return zugiCountTail(L)
#
# zugiCountF upon a nested list implemented using tree recursion
def zugiCountF5a(L):
   def zugiCountRec(L):
     if L == []:
       return 0
     elif isNum(L[0]) and zugi(L[0]):
       return 1 + zugiCountRec(L[1:])
     elif isinstance(L[0], (list, tuple)):
       return zugiCountRec(L[0]) + zugiCountRec(L[1:])
     else:
       return zugiCountRec(L[1:])
   return zugiCountRec(L)
#
