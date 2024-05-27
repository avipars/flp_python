#
# quadratic3.py
#
# This program computes the roots of a quadratic equation
#
import math

def CalculateDiscriminant(x,y,z):
   desc = y**2 - 4*x*z 
   return desc
 
def CalculateRoots(a,b,desc):
  if desc == 0:
    result = -b / (2*a)
  elif desc > 0:
    delta = math.sqrt(desc)
    term1 = -b / (2*a)
    term2 = delta / (2*a)
    root1 = term1 + delta
    root2 = term2 - delta
    result = root1, root2
  else:
    result = None
  return result

def PrintSolution(Roots):
  if (Roots == None):
    print ('no real solutions')
  elif isinstance(Roots, (int, float)):
    print ('the only one solution is ',)
    print (Roots)
  else:
    print ('the two real solutions are: ',)
    print (Roots)

a = float(input('Enter the value of a: '))
b = float(input('Enter the value of b: '))
c = float(input('Enter the value of c: '))
Desc = CalculateDiscriminant(a,b,c)
# Solution is a pair of values or only one
Solution = CalculateRoots(a,b,Desc)
PrintSolution(Solution)

##================= RESTART: P:\quadratic3.py ==========
##Enter the value of a: 5.0
##Enter the value of b: 5.0
##Enter the value of c: 1.0
##the two real solutions are: 
##(1.7360679774997898, -2.0124611797498106)
