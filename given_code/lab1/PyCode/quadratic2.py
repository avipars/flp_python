#
# quadratic2.py
#
# This program computes the roots of a quadratic equation
#
import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

desc = b**2 - 4*a*c
if desc == 0:
  root = -b / (2*a)
  print ("the only one real solution is ", root)
elif desc > 0:
  delta = math.sqrt(desc)
  term1 = -b / (2*a)
  term2 = delta / (2*a)
  root1 = term1 + delta
  root2 = term2 - delta
  print ("the two real solutions are: ", root1, root2)
else:
  print ("no real solutions")

##================= RESTART: P:\quadratic2.py =================
##Enter the value of a: 5.0
##Enter the value of b: 5.0
##Enter the value of c: 1.0
##the two real solutions are:  1.7360679774997898 -2.0124611797498106

