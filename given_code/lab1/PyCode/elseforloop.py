#
# elseforloop.py
#
import sys
import collections
#
L = eval(input('Enter a sequence of numbers: '))
if isinstance(L, collections.Iterable):
  print ('OK - the input ', L, ' is a sequence.')
else:
  prtError('ERROR - the input is not a sequence!')
  sys.exit()
#
for item in L:
   if not isinstance(item, (int, float)):
     print('ERROR - the item in position ' + str(L.index(item)) + ' is not a number')
     print ('Program is aborted')
     sys.exit()
else :
    print ('OK - all the items in the sequence are numbers')
    print ('The minimum of all of them is: ', min(L))
    print ('The maximum of all of them is: ', max(L))
    print ('The sum of all of them is: ', sum(L))
    avg = sum(L) / len(L)
    print ('The average of all of them is: ', avg)

## RESTART: P:\elseforloop.py 
##Enter a sequence of numbers: range(5)
##OK - the input  range(0, 5)  is a sequence.
##OK - all the items in the sequence are numbers
##The minimum of all of them is:  0
##The maximum of all of them is:  4
##The sum of all of them is:  10
##The average of all of them is:  2.0

## RESTART: P:\elseforloop.py 
##Enter a sequence of numbers: (1,4,'B',3)
##OK - the input  (1, 4, 'B', 3)  is a sequence.
##ERROR - the item in position 2 is not a number
##Program is aborted
