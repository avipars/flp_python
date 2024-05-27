#
# quadratic1.py
#
# This program computes the roots of a quadratic equation
# NOTE: sometimes the program may crash
#
import math

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
c = float(input("Enter the value of c: "))

desc = b**2 - 4*a*c
delta = math.sqrt(desc)
root1 = (-b + delta) / (2*a)
root2 = (-b - delta) / (2*a)

print ("The solutions are: ", root1, root2)

##================= RESTART: P:\quadratic1.py =================
##Enter the value of a: 5.0
##Enter the value of b: 5.0
##Enter the value of c: 1.0
##The solutions are:  -0.276393202250021 -0.7236067977499789
##>>>

