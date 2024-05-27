#
# reverse.py -- computes the reverse of
#               the top level of a sequence
#
from tailrecurse import *
#
def recReverse(L):
   if L == []:
     return L
   return ([L[-1]] + recReverse(L[:-1]))

def tailReverse(L, resL = []):
   if L == []:
     return resL
   return tailReverse(L[:-1], resL + [L[-1]])

#------------------
##print( recReverse(L) )
##print( tailReverse(L) )
