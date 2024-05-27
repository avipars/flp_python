#
# defaultPrm.py
#
import sys
#
def accFunc(stop, init = 0, step = 1):
   acc = 0
   for value in range(init, stop, step):
      acc += value
   return acc
#
initValStr = input("Enter the range initial value [0] : ")
stopValStr = input("Enter the range stop value : ")
if not stopValStr:
  print ('ERROR - the stop value is not optional!')
  print ('        Program is aborted')
  sys.exit()
stopVal = int(stopValStr)
stepValStr = input("Enter the range step value [1] : ")
if not initValStr:
  if stepValStr == '':
    acc = accFunc(stopVal)
  else:
    stepVal = int(stepValStr) 
    acc = accFunc(stopVal, 0, stepVal)
else:
  initVal = int(initValStr)
  if not stepValStr:
    acc = accFunc(stopVal, initVal)
  else:
    stepVal = int(stepValStr)
    acc = accFunc(stopVal, initVal, stepVal)
print (acc)
#

