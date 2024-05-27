#
# keyUnlimited2Prm.py
# -- a **kwargs variation of quadratic.py
#
from quadraticFuncs import *
#
def PrintSolution(RootsList):
  if (len(RootsList) == 0):
    print ('no real solutions')
  elif (len(RootsList) == 1):
    print ('the only one solution is ',)
    print (RootsList[0])
  else:
    print ('the two real solutions are: ',)
    print (RootsList)
#
def quadratic(a, b, c):
   desc = CalculateDiscriminant(a,b,c)
   return CalculateRoots(a, b, desc)
#
aValue = float(input('Enter the value of a: '))
bValue = float(input('Enter the value of b: '))
cValue = float(input('Enter the value of c: '))
coeffs = dict([('a',aValue),('b',bValue),('c',cValue)])
# Solution is a list
Solution = quadratic(**coeffs)
PrintSolution(Solution)

