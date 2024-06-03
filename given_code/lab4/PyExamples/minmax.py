#
# minmax.py  -- min and max implemented using reduce
#

from functools import *

def mymin(L):
   return reduce(lambda smallest, current : smallest if (smallest < current) else current, L)

def mymax(L):
   return reduce(lambda greatest, current : greatest if (greatest > current) else current, L)

def mysum(L):
   return reduce(lambda total, current : total + current, L)
