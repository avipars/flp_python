#
# rangeforloop.py
#
print ("=== Accumulating a range of values ===")
initVal = int(input("Enter the range initial value : "))
stopVal = int(input("Enter the range stop value: "))
stepVal = int(input("Enter the range step value>: "))
#
acc = 0
for i in range(initVal, stopVal, stepVal):
   acc += i
print ("=== The accumulated value is ",acc, " ===")
#

##>>> 
## RESTART: P:\rangeforloop.py 
##=== Accumulating a range of values ===
##Enter the range initial value : 1
##Enter the range stop value: 10
##Enter the range step value>: 2
##=== The accumulated value is  25  ===
##>>>
