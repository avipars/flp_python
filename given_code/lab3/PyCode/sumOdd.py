# sum_odd(n): number -> number
# sum_odd(n) is the sum of odd numbers from 1 to N
#
from tailrecurse import *
#
def recSum_odd(n):
   if n == 1:
     return 1
   elif n % 2 != 0:
     return n + recSum_odd(n-2)
   else:
     return recSum_odd(n-1)
#
@tail_call_optimized
def recSum_odd2(n, result = 0):
   if n == 1:
     return result+1
   elif n % 2 != 0:
     return recSum_odd2(n-2, result+n)
   else:
     return recSum_odd2(n-1, result)
#
