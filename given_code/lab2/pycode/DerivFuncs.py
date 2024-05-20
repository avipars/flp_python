#
from ComposeFuncs import *
#
# DerivFuncs.py
#
#***********************************************************
#          "symbolic" derivation of a function          
#***********************************************************
def deriv(f):
   return lambda x : (f(x + 0.0005) - f(x)) / 0.0005
#
#***********************************************************
#          "symbolic" Nth derivation of a function           
#***********************************************************
def Nderiv(f, N):
   def selfCompLst(func,N):
      Lst = []
      for i in range(N):
         Lst.insert(0,func)
      return Lst   
   derivSeq = selfCompLst(deriv, N)
   d = fullCompose(*derivSeq)(f)
   return d
#
#**************************************************************
# computing the value of a derivative for a specific value of x      
#**************************************************************
def derivCompute(f, x):
   return (f(x + 0.0005) - f(x)) / 0.0005
#

