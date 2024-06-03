#
# mymapfilter.py  -- implementing map and filter using reduce
#

from functools import *

def mymap(func, L):
   return reduce(lambda total, current : total + [func(current)], L, [])

def myfilter(func, L):
    return reduce(lambda total, current : total + ([current] if func(current) else []), L, [])

def myany(L):
    return reduce(lambda total, current : total or current, L)

def myall(L):
    return reduce(lambda total, current : total and current, L)
