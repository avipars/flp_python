#
# quadraticFuncs.py
# -- a module containing functions used by quadratic.py
#
import math

def CalculateDiscriminant(x,y,z):
   desc = y**2 - 4*x*z 
   return desc
 
def CalculateRoots(a,b,desc):
  result = []
  term = -b / (2*a)
  if desc == 0:
    result.append(term)
  elif desc > 0:
    root1 = term + math.sqrt(desc) / (2*a)
    root2 = term - math.sqrt(desc) / (2*a)
    result.extend([root1, root2]) 
  else:
    pass
  return result


