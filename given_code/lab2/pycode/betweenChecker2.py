#
# betweenChecker2.py
#
def createFunc (low, up):
   def checker(x):
      if (low <= x):
        return x
      else:
        return up
   return checker
#
f1 = createFunc (1,10)
f2 = createFunc (1,20)
#
print (f1(14), f1(0))
print (f2(14), f2(0))
#
