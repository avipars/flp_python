#
# zugiCountHOfuncs.py
#
from functools import reduce
#
def zugi(N):
   return N%2 == 0
#
def isNum(x):
   return isinstance(x,(int, float))
#
def zugiCountF(L):
   return len(list(filter(zugi, filter(isNum, L))))
#
def zugiCountM(L):
   return sum(map((lambda x : 1), filter(zugi, filter(isNum, L))))
#
def zugiCountLC1(L):
   return sum([1 for i in L  if isNum(i) and zugi(i)])
#
def zugiCountLC2(L):
   return sum([1 for i2 in [i1 for i1 in L  if isNum(i1)]  if zugi(i2)])    
#
def zugiCountR1(L):
   return reduce((lambda x,y : x+y), list(map((lambda x : 1), filter(zugi, filter(isNum, L)))))
#
def zugiCountR2(L):
   return reduce((lambda x,y : x+y), [1 for i in L  if isNum(i) and zugi(i)])
#
   
