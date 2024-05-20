#
# betweenChecker1.py
#
def createFunc (low, up):
   return lambda x : low <= x <= up
#
f1 = createFunc (1,10)
f2 = createFunc (1,20)
#
print (f1(14))
print (f2(14))
#
