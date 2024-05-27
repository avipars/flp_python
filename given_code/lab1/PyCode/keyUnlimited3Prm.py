#
# keyUnlimited3Prm.py
# -- Python file which may be used as
#    a program as well as a module
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
def main():
  aValue = float(input('Enter the value of a: '))
  bValue = float(input('Enter the value of b: '))
  cValue = float(input('Enter the value of c: '))
  coeffs = dict([('a',aValue),('b',bValue),('c',cValue)])
  # Solution is a list
  Solution = quadratic(**coeffs)
  PrintSolution(Solution)
#
if __name__ == "__main__":
  print ("Now this Python file is run as a program")
  main()
else:
  print ("Now this Python file is imported as a module")
