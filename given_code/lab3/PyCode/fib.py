#
# Tree Recursion
#
# The first N Fibonacci Numbers
#
from tailrecurse import *
#
# Using Non-Tail (Tree) Recursion
#      
def fib1(N):
   if (N == 0):
     return 0
   elif (N == 1):
     return 1
   else:
     return fib1(N-1) + fib1(N-2)
#
# Using Tail Recursion
#
def fib2(n):
  @tail_call_optimized
  def fibIter(a, b, count):
     if (count == 0):
       return  b
     else:
       return fibIter(a+b, a, count-1)
  return fibIter(1, 0, n)
#
def fib1aSeq(N):
   if N == 0:
     return [fib1(N)]
   return fib1aSeq(N-1)+[fib1(N)]
#
