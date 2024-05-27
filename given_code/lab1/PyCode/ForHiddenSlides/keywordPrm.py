#
# keywordPrm.py
#
def accFunc(init, stop, step):
   acc = 0
   for value in range(init, stop, step):
      acc += value
   return acc
#
initVal = int(input("Enter the range initial value : "))
stopVal = int(input("Enter the range stop value : "))
stepVal = int(input("Enter the range step value : "))
acc = accFunc(stop = stopVal, step = stepVal, init = initVal)
print (acc)
#
